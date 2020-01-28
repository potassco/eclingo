import sys
from eclingo.main import Eclingo


if __name__ == "__main__":
    eclingo_control = Eclingo()

    eclingo_control.print_version()
    models = 0
    for model in eclingo_control.main(sys.argv[1:]):
        models += 1
        answer = ('\t').join(['&k{ '+str(atom)+' }' for atom in model if 'aux_' in atom.name])
        answer = answer.replace('aux_', '').replace('not_', '~ ').replace('sn_', '-')
        print('Answer: %s\n%s' % (models, answer))

    if models:
        print('SATISFIABLE\n')
    else:
        print('UNSATISFIABLE\n')
    print('Elapsed time: %.6f s' % eclingo_control.elapsed_time)
