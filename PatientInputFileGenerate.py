# Kyle Saltmarsh
# kyle.saltmarsh@research.uwa.edu.au

# Patient Input File Generator
import sys
import pandas as pd
import numpy as np

def PIFG(Parameters,R,N,W):
    text_file = open(Parameters, "r")
    lines = text_file.readlines()
    text_file.close()
    SimulatedPatients = np.zeros(shape=((len(lines)+1)*N, len(lines)))
    SimulatedPatients2 = np.zeros((len(lines)+1)*N)

    # Simulate reference values
    for i in range(0,len(lines)):
        SimulatedPatients[:,i] = float(lines[i])

    # Simulate reference values
    for i in range(0,len(lines)):
        min = SimulatedPatients[0,i] - float(R)*SimulatedPatients[0,i]
        max = SimulatedPatients[0,i] + float(R)*SimulatedPatients[0,i]

        for j in range(0,N):
            SimulatedPatients[N*i+j,i] = min + j*(max-min)/(N-1)

    df1 = pd.DataFrame(SimulatedPatients, columns = (
    'Bone', 'neo_Hookean_tendon', 'muscle', 'fat', 'skin', 'Ogeden_Tendon_A', 'Ogeden_Tendon_B', 'Ogeden_Tendon_C',
    'Ogeden_Muscle_A', 'Ogeden_Muscle_B', 'Ogeden_Muscle_C', 'Ogeden_Fat_A', 'Ogeden_Fat_B', 'Ogeden_Fat_C',
    'Ogeden_Skin_A', 'Ogeden_Skin_B', 'Ogeden_Skin_C'))

    # Simulate reference values
    min = float(W) - float(R) * float(W)
    max = float(W) + float(R) * float(W)
    SimulatedPatients2[:] = float(W )

    for j in range(0,5):

        SimulatedPatients2[len(lines)*N + j] = min + j*(max-min)/(N-1)

    subjectname = 'Simulated Patient'
    df2 = pd.DataFrame({'Subject Name': subjectname, 'Weight': SimulatedPatients2})

    return df1,df2

df1,df2 = PIFG(sys.argv[1],float(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4]))

df1.to_csv('SimulatedPatientsperryinfo.csv', index=False)
df2.to_csv('SimulatedPatientssubinfo.csv', index=False)
