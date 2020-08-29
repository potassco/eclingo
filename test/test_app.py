import os
from os import register_at_fork
import subprocess
import unittest

from clingo import Number
import eclingo
from eclingo.util.logger import silent_logger


APP_PATH = '../eclingo/main.py'

INPUT_PROG_PATH = 'prog/input/'
OUTPUT_PROG_PATH = 'prog/output/'

KB_ELIGIBLE_PATH = 'eligible/eligible.lp'
INPUT_ELIGIBLE_PATH = 'eligible/input/'
OUTPUT_ELIGIBLE_PATH = 'eligible/output/'

KB_YALE_PATH = 'yale/yale.lp'
INPUT_YALE_PATH = 'yale/input/'
OUTPUT_YALE_PATH = 'yale/output/'


def parse_output(output):
    lines = output.split('\n')
    world_views = []
    is_world_view = False
    for line in lines:
        if is_world_view:
            world_view = line.split()
            world_views.append(world_view)
            is_world_view = False
        elif line.startswith('World view:'):
            is_world_view = True
    return world_views


class TestExamples(unittest.TestCase):

    def assert_world_views(self, command, output_path):
        process = subprocess.Popen(command,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode('utf-8')
        # print(stderr.decode('utf-8'))
        world_views = parse_output(output)
        for world_view in world_views:
            world_view.sort()
        world_views.sort()
        world_views = [str(wv) for wv in world_views]
        world_views = str(world_views).replace(' ', '').replace("'", '').replace('"', '')
        
        with open(output_path, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        self.assertEqual(world_views, sol, 'in ' + str(command))
    
    
    def test_prog_g94(self):
        for i in range(1, 11):
            path = os.path.dirname(os.path.realpath(__file__))
            input_path = os.path.join(path, INPUT_PROG_PATH)
            input_path = os.path.join(input_path, f'prog{i:02d}.lp')
            output_path = os.path.join(path, OUTPUT_PROG_PATH)
            output_path = os.path.join(output_path, f'sol{i:02d}.txt')
            app_path = os.path.join(path, APP_PATH)

            command = ['python', app_path, '0', input_path]
            self.assert_world_views(command, output_path)


    def test_eligible_g94(self):
        for i in range(1, 17):
            path = os.path.dirname(os.path.realpath(__file__))
            elegible_path = os.path.join(path, KB_ELIGIBLE_PATH)
            input_path = os.path.join(path, INPUT_ELIGIBLE_PATH)
            input_path = os.path.join(input_path, f'eligible{i:02d}.lp')
            output_path = os.path.join(path, OUTPUT_ELIGIBLE_PATH)
            output_path = os.path.join(output_path, f'sol_eligible{i:02d}.txt')
            app_path = os.path.join(path, APP_PATH)

            command = ['python', app_path, '0', elegible_path, input_path]
            self.assert_world_views(command, output_path)


    def test_yale_g94(self):
        for i in range(1, 9):
            if i != 6:
                path = os.path.dirname(os.path.realpath(__file__))
                yale_path  =  os.path.join(path, KB_YALE_PATH)
                input_path =  os.path.join(path, INPUT_YALE_PATH)
                input_path =  os.path.join(input_path, f'yale{i:02d}.lp')
                output_path = os.path.join(path, OUTPUT_YALE_PATH)
                output_path = os.path.join(output_path, f'sol_yale{i:02d}.txt')

                app_path = os.path.join(path, APP_PATH)

                constant = '-c length=%d' % i
                command = ['python', app_path, constant, '0', yale_path, input_path]
                self.assert_world_views(command, output_path)
