import python_actr   
from python_actr import *
import csv

#------------------------------------------------------

### MMRT PROBLEM #66 ###

# P1) Edwards is below and to the left of Derek
# P2) Derek is below and to the left of Travis
# P3) Travis is below and to the left of Brian
# C) Edward is below and to the left of Brian

# Avg_Acc: 0.739130435
# Avg_RT: 36.09855072
# Relation: Spatial
# Premise: Three
# Dimensions: Two
# Answer: True
# Solution: True
# Premise Order: Continuous
# CPhrasing: Afirst

# Accumulated number of spatial focus to solve: 16

# C:\Users\turca\Documents\2-coding_projects\5-ICCM-pyv310\python_actr-main> FOR /l %i in (1,1,310) DO python 04-3P2D_MMRT.py

# FOR 3
# FOR /l %i in (1,1,930) DO python 04-3P2D_ICCM.py

# FOR 10
# FOR /l %i in (1,1,3100) DO python 04-3P2D_ICCM.py

# FOR 30
# FOR /l %i in (1,1,10000) DO python 04-3P2D_ICCM.py


# ------------------------------------------------------

class MyEnvironment(python_actr.Model):
    pass


class MyAgent(ACTR):

    spatial_focus=Buffer()
    goal_focus=Buffer()
    DMbuffer=Buffer()

    production_time=0.05
    production_sd=0.01
#    production_threshold = 0.0

    DM=Memory(DMbuffer, latency=0.05, threshold=0.3, maximum_time=10.0, finst_size=0, finst_time=3.0)
    DMN=DMNoise(DM, noise=0.3, baseNoise=0.3)
    DMD=DMBaseLevel(DM, decay=0.5, limit=None)

    dm_spread=DMSpreading(DM,goal_focus)
    dm_spread.strength=1
    dm_spread.weight[goal_focus]=0.0

    partial=Partial(DM,strength= 0.0, limit= 0.0)
    partial.similarity('edward','derek', 0)
    partial.similarity('edward','travis', 0)
    partial.similarity('edward','brian', 0 )

    partial.similarity('derek','travis', 0)
    partial.similarity('derek','brian', 0)

    partial.similarity('travis','brian', 0)

#####-----------------------CONSTRUCTION-------------------------------------#####

    goal_focus.set('read_premise_1')
    spatial_focus.set('object:na location:na direction:na')

    # 1-construction-read_premise
    def read_premise_1(goal_focus='read_premise_1',spatial_focus='object:na location:na direction:na'):
        print('Premise 1: Edwards is below and to the left of Derek (1)')
        spatial_focus.set('object:na location:0.0 direction:na')
        goal_focus.set('insert_edward_2')
   
    # 2-construction-insert_edward
    def insert_edward_2(goal_focus='insert_edward_2',spatial_focus='object:na location:0.0 direction:na'):
        print('Insert Edward (2)')
        DM.threshold+=.09
        DM.add('object:edward location:0.0 annotation:na')
        spatial_focus.set('object:edward location:0.0 direction:na')
        goal_focus.set('move_above_3')

    # 3-construction-move_above
    def move_above_3(goal_focus='move_above_3',spatial_focus='object:edward location:0.0 direction:na'):
        print('Move above (3)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:0.1 direction:above')
        goal_focus.set('move_right_4')
    
    # 4-construction-move_right
    def move_right_4(goal_focus='move_right_4',spatial_focus='object:na location:0.1 direction:above'):
        print('Move right (4)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:1.1 direction:right')
        goal_focus.set('insert_derek_5')
    
    # 5-construction-insert_derek
    def insert_derek_5(goal_focus='insert_derek_5',spatial_focus='object:na location:1.1 direction:right'):
        print('Insert Derek (5)')
        DM.threshold+=.09
        DM.add('object:derek location:1.1 annotation:na')
        spatial_focus.set('object:derek location:1.1 direction:right')
        goal_focus.set('read_premise_6')
    
    # 6-construction-read_premise
    def read_premise_6(goal_focus='read_premise_6',spatial_focus='object:derek location:1.1 direction:right'):
        print('Premise 2: Derek is below and to the left of Travis (6)')
        spatial_focus.set('object:derek location:1.1 direction:right')
        goal_focus.set('move_above_7')
    
    # 7-construction-move_above
    def move_above_7(goal_focus='move_above_7',spatial_focus='object:derek location:1.1 direction:right'):
        print('Move above (7)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.1 direction:above')
        goal_focus.set('move_right_8')
    
    # 8-construction-move_right
    def move_right_8(goal_focus='move_right_8',spatial_focus='object:na location:2.1 direction:above'):
        print('Move right (8)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.2 direction:right')
        goal_focus.set('insert_travis_9')
    
    # 9-construction-insert_travis
    def insert_travis_9(goal_focus='insert_travis_9',spatial_focus='object:na location:2.2 direction:right'):
        print('Insert Travis (9)')
        DM.threshold+=.09
        DM.add('object:travis location:2.2 annotation:na')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('read_premise_10')

    # 10-construction-read_premise
    def read_premise_10(goal_focus='read_premise_10',spatial_focus='object:travis location:2.2 direction:right'):
        print('Premise 3: Travis is below and to the left of Brian (10)')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('move_above_11')
    
    # 11-construction-move_above
    def move_above_11(goal_focus='move_above_11',spatial_focus='object:travis location:2.2 direction:right'):
        print('Move above (11)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:3.2 direction:above')
        goal_focus.set('move_right_12')
    
    # 12-construction-move_right
    def move_right_12(goal_focus='move_right_12',spatial_focus='object:na location:3.2 direction:above'):
        print('Move right (12)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:3.3 direction:right')
        goal_focus.set('insert_brian_13')

    # 13-construction-insert_brian 
    def insert_brian_13(goal_focus='insert_brian_13',spatial_focus='object:na location:3.3 direction:right'):
        print('Insert Brian (13)')
        DM.threshold+=.09
        DM.add('object:brian location:3.3 annotation:na')
        spatial_focus.set('object:brian location:3.3 direction:right')
        goal_focus.set('read_conclusion_14')
    

######---------------------INSPECT-----------------------------#######

    # This function is used to write the conclusions True(1)/False(0) to a csv file
    # FOR /l %i in (1,1,100) DO python 0-2P1D-MMRT.py
    def decision (self,answer):
        myfile=open("3P2D-thresh-09.csv", "a", newline="")
        wr=csv.writer(myfile)
        wr.writerow(answer)
        myfile.close()

    #14-inspection-read_conclusion
    def read_conclusion_14(goal_focus='read_conclusion_14',spatial_focus='object:brian location:3.3 direction:right'):
        print('Conclusion: Edward is below and to the left of Brian (14)')
        spatial_focus.set('object:brian location:3.3 direction:right')
        goal_focus.set('request_edward_15')
    

    #15-inspection-request_edward
    def request_edward_15(goal_focus='request_edward_15',spatial_focus='object:brian location:3.3 direction:right'):
        print('Recalling Edwards location...(15)')
        DM.request('object:edward location:!3.3') # !3.3 because spatial_focus is already on this location
        spatial_focus.set('object:brian location:3.3 direction:right') # spatial_focus still on Brian after construction
        goal_focus.set('recall_edward_16A1B1C1D1') # to allow branching, all possible productions have the same value in their buffers which then change to continue down the selected branch path

##########################################################################

#-----------------BRANCH-16-A1-B1-C1-D1---------------------------------

##########################################################################

#--------16A1-Correct Recall of Edwards Position--------------

    #16A1-inspection-recall_correct
    def recall_correct_16A1(goal_focus='recall_edward_16A1B1C1D1',spatial_focus='object:brian location:3.3 direction:right', DMbuffer='location:0.0'):
        print('I recall Edward is at location 0.0 (recall_correct) (16A1)')
        spatial_focus.set('object:brian location:3.3 direction:right')
        goal_focus.set('move_below_16A2')
    
    #16A2-inspection-move_below
    def move_below_16A2(goal_focus='move_below_16A2',spatial_focus='object:brian location:3.3 direction:right'):
        print('Move below (16A2)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:3.2 direction:below')
        goal_focus.set('move_left_16A3')

    #16A3-inspection-move_left
    def move_left_16A3(goal_focus='move_left_16A3',spatial_focus='object:na location:3.2 direction:below'):
        print('Move left (16A3)')
        DM.threshold+=.09
        spatial_focus.set('object:travis location:2.2 direction:left')
        goal_focus.set('move_below_16A4')

    #16A4-inspection-move_below
    def move_below_16A4(goal_focus='move_below_16A4',spatial_focus='object:travis location:2.2 direction:left'):
        print('Move below (16A4)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.1 direction:below')
        goal_focus.set('move_left_16A5')

    #16A5-inspection-move_left
    def move_left_16A5(goal_focus='move_left_16A5',spatial_focus='object:na location:2.1 direction:below'):
        print('Move left (16A5)')
        DM.threshold+=.09
        spatial_focus.set('object:travis location:1.1 direction:left')
        goal_focus.set('move_below_16A6')
    
    #16A6-inspection-move_below
    def move_below_16A6(goal_focus='move_below_16A6',spatial_focus='object:travis location:1.1 direction:left'):
        print('Move below (16A6)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:1.0 direction:below')
        goal_focus.set('move_left_16A7')

    #16A7-inspection-move_left
    def move_left_16A7(goal_focus='move_left_16A7',spatial_focus='object:na location:1.0 direction:below'):
        print('Move left (16A7)')
        DM.threshold+=.09
        spatial_focus.set('object:edward location:0.0 direction:left')
        goal_focus.set('confirm_conclusion_16A8')

    #16A8-inspection-confirm_conclusion
    def confirm_conclusion_16A8(goal_focus='confirm_conclusion_16A8',spatial_focus='object:edward location:0.0 direction:left'):
        print('True, Edward is below and to the left of Brian! (recall_correct) (16A8)')
        self.decision('1')
        self.stop()

#######################################################################

###---------16B1-Omission Recall Error of Edwards Position----------###

    #16B1-inspection-recall_omission
    def recall_omission_16B1(goal_focus='recall_edward_16A1B1C1D1', spatial_focus='object:brian location:3.3 direction:right', DM='error:True',DMbuffer=None):
        print('I can not recall Edwards location (recall_omission) (16B1)')
        spatial_focus.set('object:brian location:3.3 direction:right')
        goal_focus.set('confirm_conclusion_16B2A1B1')

        
#---------16B1-A1-B1----------------------------------------

    #16B1A1-inspection-confirm_conclusion
    def confirm_conclusion_16B2A1(goal_focus='confirm_conclusion_16B2A1B1',spatial_focus='object:brian location:3.3 direction:right'):
        print('True, Edward is below and to the left of Brian! (recall_omission) (16B2A1)')
        self.decision('1')
        self.stop()


    #16B1B1-inspection-confirm_conclusion
    def confirm_conclusion_16B2B1(goal_focus='confirm_conclusion_16B2A1B1',spatial_focus='object:brian location:3.3 direction:right'):
        print('False, Edward is NOT below and to the left of Brian! (recall_omission) (16B2B1)')
        self.decision('0')
        self.stop()
        
######################################################################

###-----16C1-Commission Recall Error of Edwards Position as Travis-----###


    #16C1-inspection-recall_commission...travis
    def recall_commission_16C1 (goal_focus='recall_edward_16A1B1C1D1',spatial_focus='object:brian location:3.3 direction:right',DMbuffer='location:2.2'):
        print('I recall Edward is at location 2.2 (recall_commission) (16C1)')
        spatial_focus.set('object:brian location:3.3 direction:right')
        goal_focus.set('move_below_16C2')
    
    #16C1A2-inspection-move_below
    def move_below_16C2(goal_focus='move_below_16C2',spatial_focus='object:brian location:3.3 direction:right'):
        print('Move below (16C2)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:3.2 direction:below')
        goal_focus.set('move_left_16C3')

    #16C1A3-inspection-move_left
    def move_left_16C3(goal_focus='move_left_16C3',spatial_focus='object:na location:3.2 direction:below'):
        print('Move left (16C3)')
        DM.threshold+=.09
        spatial_focus.set('object:travis location:2.2 direction:left')
        goal_focus.set('confirm_conclusion_16C4')

    #16C1A4-confirm_conclusion
    def confirm_conclusion_16C4(goal_focus='confirm_conclusion_16C4',spatial_focus='object:travis location:2.2 direction:left'):
        print('True, Edward is below and to the left of Brian! (recall_commission...travis) (16C4)')
        spatial_focus.set('object:travis location:2.2 direction:left')
        self.decision('1')
        self.stop()

#------16D1-Commission Recall Error of Edwards position as Dereks---------

    #16D1-inspection-recall_commission...derek
    def recall_commission_16D1(goal_focus='recall_edward_16A1B1C1D1',spatial_focus='object:brian location:3.3 direction:right',DMbuffer='location:1.1'):
        print('I recall Edward is at location 1.1 (recall_commission) (16D1)')
        spatial_focus.set('object:brian location:3.3 direction:right')
        goal_focus.set('move_below_16D2')
    
    #16D2-inspection-move_below
    def move_below_16D2(goal_focus='move_below_16D2',spatial_focus='object:brian location:3.3 direction:right'):
        print('Move below (16D2)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:3.2 direction:below')
        goal_focus.set('move_left_16D3')

    #16D3-inspection-move_left
    def move_left_16D3(goal_focus='move_left_16D3',spatial_focus='object:na location:3.2 direction:below'):
        print('Move left (16D3)')
        DM.threshold+=.09
        spatial_focus.set('object:travis location:2.2 direction:left')
        goal_focus.set('move_below_16D4')

    #16D4-inspection-move_below
    def move_below_16D4(goal_focus='move_below_16D4', spatial_focus='object:travis location:2.2 direction:left'):
        print('Move below (16D4)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.1 direction:below')
        goal_focus.set('move_left_16D5')

    #16C1B5-inspection-move_left
    def move_left_16D5(goal_focus='move_left_16D5',spatial_focus='object:na location:2.1 direction:below'):
        print('Move left (16D5)')
        DM.threshold+=.09
        spatial_focus.set('object:derek location:1.1 direction:left')
        goal_focus.set('confirm_conclusion_16D6')

    #16C1B6-inspection-confirm_conclusion
    def confirm_conclusion_16D6(goal_focus='confirm_conclusion_16D6',spatial_focus='object:derek location:1.1 direction:left'):
        print('True, Edward is below and to the left of Brian! (recall_commission...derek) (16D6)')
        spatial_focus.set('object:derek location:1.1 direction:left')
        self.decision('1')
        self.stop()



################################################################


nico = MyAgent()
thesis = MyEnvironment()
thesis.agent=nico
python_actr.log_everything(thesis)
thesis.run()
python_actr.finished()

