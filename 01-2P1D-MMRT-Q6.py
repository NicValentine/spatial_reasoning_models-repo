import python_actr   
from python_actr import *
import csv

#------------------------------------------------------

# 2P1D - MMRT - Q # 6 (COMPLETE)

# P1) Edward is to the left of Derek.
# P2) Derek is to the left of Travis.
# C) EDWARD IS TO THE LEFT OF TRAVIS.

# Avg_Acc : 0.835748792
# Avg_RT : 26.36728502
# Relation: Spatial
# Premises: Two Premises
# Dimensions: One Dimension
# Answer: True
# Solution: True
# Premise Order: Continuous
# CPhrasing: Afirst

# Accumulated number of operations of the sapatial focus to solve : 7

# COMMAND LINE 
# C:\Users\turca\ Documents\2-coding_projects\5-ICCM-pyv310\python_actr-main> FOR /l %i in (1,1,310) DO python 01-2P1D_MMRT.py

# FOR 3
# FOR /l %i in (1,1,930) DO python 01-2P1D_ICCM.py

# FOR 5
# FOR /l %i in (1,1,1550) DO python 01-2P1D_ICCM.py

# FOR 30
# FOR /l %i in (1,1,10000) DO python 01-2P1D_ICCM.py

# ------------------------------------------------------

class MyEnvironment(python_actr.Model):
    pass


class MyAgent(ACTR):

    spatial_focus=Buffer()
    goal_focus=Buffer()
    DMbuffer=Buffer()

    production_time=0.05
    production_sd=0.01
 #   production_threshold = 0.05 # this stops the agent from running? wut?

    DM=Memory(DMbuffer, latency=0.05, threshold=0.3, maximum_time=10.0, finst_size=0, finst_time=3.0) # default threshold 0.3
    DMN=DMNoise(DM, noise=0.3, baseNoise=0.3) # noise & basenoise default = 0.3 
    DMBaseLevel(DM, decay=0.5, limit=None) # decay default = 0.5

    dm_spread=DMSpreading(DM,goal_focus)
    dm_spread.strength=1
    dm_spread.weight[goal_focus]=0.0

    partial=Partial(DM,strength= 0.0, limit= 0.0)
    partial.similarity('edward', "derek", 0)
    partial.similarity('travis', 'derek', 0)
    partial.similarity('edward', 'travis', 0)



#####-----------------------CONSTRUCTION-------------------------------------#####

    goal_focus.set('read_premise_1')
    spatial_focus.set('object:na location:na direction:na')

    # 1-construction-read_premise
    def read_premise_1 (goal_focus='read_premise_1', spatial_focus='object:na location:na direction:na'):    
        print('Premise 1: Edward is to the left of Derek.')
        spatial_focus.set('object:na location:na direction:na')
        goal_focus.set('insert_edward_2')
    
    # 2-construction-insert_edward
    def insert_edward_2 (goal_focus='insert_edward_2', spatial_focus='object:na location:na direction:na'):
        print("Insert Edward")
        DM.threshold+=.09
        DM.add('object:edward location:0.0 annotation:na') 
        spatial_focus.set('object:edward location:0.0 direction:na') # (E)
        goal_focus.set('move_right_3')

    # 3-construction-move_right
    def move_right_3 (goal_focus='move_right_3', spatial_focus='object:edward location:0.0 direction:na'):
        print("Move right")
        DM.threshold+=.09
        spatial_focus.set('object:na location:1.0 direction:right') # E ()
        goal_focus.set('insert_derek_4')
    
    # 4-construction-insert_derek
    def insert_derek_4 (goal_focus='insert_derek_4', spatial_focus='object:na location:1.0 direction:right'):
        print("Insert Derek")
        DM.threshold+=.09
        DM.add('object:derek location:1.0 annotation:na') 
        spatial_focus.set('object:derek location:1.0 direction:right') # E (D)
        goal_focus.set('read_premise_5')

    # 5-construction-read_premise
    def read_premise_5 (goal_focus='read_premise_5', spatial_focus='object:derek location:1.0 direction:right'):
        print('Premise 2: Derek is to the left of Travis')
        spatial_focus.set('object:derek location:1.0 direction:right')
        goal_focus.set('move_right_6')

    # 6-construction-move_right
    def move_right_6 (goal_focus='move_right_6', spatial_focus='object:derek location:1.0 direction:right'):
        print("Move right")
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.0 direction:right') # E D ()
        goal_focus.set("insert_travis_7")
    
    # 7-construction-insert_travis
    def insert_travis_7 (goal_focus='insert_travis_7', spatial_focus='object:na location:2.0 direction:right'):
        print("Insert Travis")
        DM.threshold+=.09
        DM.add('object:travis location:2.0 annotation:na') 
        spatial_focus.set('object:travis location:2.0 direction:right') # E D (T)
        goal_focus.set('read_conclusion_8')


######---------------------INSPECT-----------------------------#######

    # This function is used to write the conclusions True(1)/False(0) to a csv file
    # FOR /l %i in (1,1,100) DO python 0-2P1D-MMRT.py
    def decision (self,answer):
        myfile=open("2P1D-thresh-09.csv", "a", newline="")
        wr=csv.writer(myfile)
        wr.writerow(answer)
        myfile.close()

    # 8-inspection-read_conclusion
    def read_conclusion_8 (goal_focus='read_conclusion_8', spatial_focus='object:travis location:2.0 direction:right'): 
        print('Conclusion: Edward is to the left of Travis')
        spatial_focus.set('object:travis location:2.0 direction:right') # spatial_focus still on Travis after construction : E D (T)
        goal_focus.set('request_edward_9')

    # 9-inspection-request_edward
    def request_edward_9 (goal_focus='request_edward_9', spatial_focus='object:travis location:2.0 direction:right'):
        print("Recalling Edward's location...(9)")
        DM.request('object:edward location:!2.0') #!2.0 because spatial spatial_focus is already on this location
        spatial_focus.set('object:travis location:2.0 direction:right')
        goal_focus.set('recall_edward_10A1B1C1') 
        # to allow branching, all possible productions have the same value in their buffers which then change to continue down the selected branch path

### Branch ###

###-----Correct Recall of Edwards Position-----###

    # 10A1-inspection-recall_correct
    def recall_correct_10A1 (goal_focus='recall_edward_10A1B1C1', spatial_focus='object:travis location:2.0 direction:right',  DMbuffer='location:0.0'):
        print('Edward is at location 0.0 (recall_correct) (10A1).')
        spatial_focus.set('object:travis location:2.0 direction:right')
        goal_focus.set('move_left_10A2')

    # 10A2-inspection-move_left
    def move_left_10A2 (goal_focus='move_left_10A2', spatial_focus='object:travis location:2.0 direction:right'):
        print("Move left, spatial focus on Derek (recall_correct) (10A2).")
        DM.threshold+=.09
        spatial_focus.set('object:derek location:1.0 direction:left') # E (D) T
        goal_focus.set('move_left_10A3')

    # 10A3-inspection-move_left
    def move_left_10A3 (goal_focus='move_left_10A3', spatial_focus='object:derek location:1.0 direction:left'):
        print('Move left, spatial focus on Travis. (recall_correct) (10A3)')
        DM.threshold+=.09
        spatial_focus.set('object:edward location:0.0 direction:left') # (E) D T
        goal_focus.set('confirm_conclusion_10A4')

    # 10A4-inspection-confirm_conclusion (TRUE)
    def confirm_conclusion_10A4 (goal_focus='confirm_conclusion_10A4', spatial_focus='object:edward location:0.0 direction:left'):
        print("True, Edward is to the left of Travis (recall_correct) (10A4).")
        self.decision('1')
        self.stop()



###-----Error of Omission of Edwards Position-----###

    # 10B1-inspection-recall_omission
    def recall_omission_10B1 (goal_focus='recall_edward_10A1B1C1', spatial_focus='object:travis location:2.0 direction:right', DM='error:True', DMbuffer=None): # spatial_focus still on Travis after construction : E D (T)
        print("I don't remember the Edward's location (recall_omission)") # introduces need for theories about micro-strategies, in these models we assume a 50/50 chance decision. 
        spatial_focus.set('object:travis location:2.0 direction:right')
        goal_focus.set('confirm_conclusion_10B2A1B1') #to allow branching

### Branch ###

    # 10B1A1-inspection-confirm_conclusion (TRUE)
    def confirm_conclusion_10B2A1 (goal_focus='confirm_conclusion_10B2A1B1', spatial_focus='object:travis location:2.0 direction:right'):
        print('True, Edward is to the left of Travis (recall_omission-10B2A1)') 
        self.decision('1')
        self.stop()


    # 10B1B1-inspection-confirm_conclusion (FALSE)
    def confirm_conclusion_10B2B1 (goal_focus='confirm_conclusion_10B2A1B1', spatial_focus='object:travis location:2.0 direction:right'):
        print('False, Edward is not to the left of Travis (recall_omission-10B2B1)')
        self.decision('0')
        self.stop()


###-----Error of Commission of Edwards Position for Derek-----###

    # 10C1-inspection-recall_commission
    def recall_commission_C1 (goal_focus='recall_edward_10A1B1C1', spatial_focus='object:travis location:2.0 direction:right',  DMbuffer='location:1.0'):
        print('I recall Edwards location to be 1.0 (recall_commission) (Derek location)')
        spatial_focus.set('object:travis location:2.0 direction:right')
        goal_focus.set('move_left_10C2')

    # 10C2-inspection-move_left
    def move_left_10C2 (goal_focus='move_left_10C2', spatial_focus='object:travis location:2.0 direction:right'):
        print('Move left')
        DM.threshold+=.09
        spatial_focus.set('object:derek location:1.0 direction:left') # E (D) T
        goal_focus.set('confirm_conclusion_10C3')
    
    # 10C3-inspection-confirm_conclusion
    def confirm_conclusion_10C3 (goal_focus='confirm_conclusion_10C3', spatial_focus='object:derek location:1.0 direction:left'):
        print('True, Edward is Left of Travis (recall_commission-10C3)') # E (D) T
        self.decision('1')
        self.stop()



################################################################


nico = MyAgent()
thesis = MyEnvironment()
thesis.agent=nico
python_actr.log_everything(thesis)
thesis.run()
python_actr.finished()

