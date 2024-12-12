#!/usr/bin/env python3
import os

for i in range(1, 251, 10):
    os.system(f"mkdir -p instances")
    os.system(
        f"./generate-nseq-ordered.py {i} | plasp translate > instances/instance_{i:03}.lp"
    )
    os.system(f"printf '\nhorizon({i}).' >> instances/instance_{i:03}.lp")
    # os.system(f"sed -e '/plasp_output/r ../experiment/instance-{i}' ../sequential-horizon.uurev.qasp | sed -e 's/@@horizon@@/{i}/g' > ../experiment/instance-{i}.sat.qasp" )
    # os.system(f"eclingo 0 --stats -c horizon={i} ../experiment/instance-{i} ../sequential-horizon.uurev.general.eclingo")
    # os.system(f"eclingo --stats -c horizon={i} ../experiment/instance-{i} ../sequential-horizon.uurev.general.eclingo")
#     os.system(f"./pyrunlim.py -t 1200 -m 16384 -s 0 'eclingo -c horizon={i} ../experiment/instance-{i} ../sequential-horizon.uurev.eclingo' >& ../experiment/ordered.{i}.{i}.elp.simple.pyrunlim")
#     os.system(f"./pyrunlim.py -t 1200 -m 16384 -s 0 'clingo -c horizon={i} ../experiment/instance-{i} ../sequential-horizon.uurev.sat.lp' >& ../experiment/ordered.{i}.{i}.asp.general.pyrunlim")
#     os.system(f"./pyrunlim.py -t 1200 -m 16384 -s 0 'clingo -c horizon={i} ../experiment/instance-{i} ../sequential-horizon.uurev.lp' >& ../experiment/ordered.{i}.{i}.asp.simple.pyrunlim")
#     os.system(f"./pyrunlim.py -t 1200 -m 16384 -s 0 'java -jar qasp.jar -n 0 -f chosen,plan ../experiment/instance-{i}.sat.qasp' >& ../experiment/ordered.{i}.{i}.qasp.pyrunlim")

# RUN
# eclingo 0 instances/instance_{i} sequential-horizon.uurev.eclingo.lp
