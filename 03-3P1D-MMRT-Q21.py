import python_actr   
from python_actr import *
import csv

#------------------------------------------------------ 

### PROBLEM Q21 MMRT ###

# P1) Edward is to the left of Derek.
# P2) Derek is to the left of Travis.
# P3) Travis is to the left of Brian.
# C) EDWARD IS TO THE LEFT OF BRIAN.


# Relation: Spatial
# Premise: Three
# Dimensions: One
# Answer: True
# Solution: True
# Premise Order: Continuous
# CPhrasing: Afirst
# Avg_Acc: 0.790322581
# Avg_RT: 29.98980645

# Accumulated number of moves of spatial focus to answer : 10

# C:\Users\turca\Documents\2-coding_projects\5-ICCM-pyv310\python_actr-main> FOR /l %i in (1,1,310) DO python 03-3P1D_MMRT.py

# FOR 5 
# FOR /l %i in (1,1,2170) DO python 03-3P1D_ICCM.py

# FOR 30
# FOR /l %i in (1,1,10000) DO python 03-3P1D_ICCM.py

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
    DMBaseLevel(DM, decay=0.5, limit=None)

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
    def read_premise_1(goal_focus='read_premise_1', spatial_focus='object:na location:na direction:na'):
        print('Premise 1: Edward is to the left of Derek.')
        spatial_focus.set('object:na location:na direction:na')
        goal_focus.set('insert_edward_2')
    
    # 2-construction-insert_edward
    def insert_edward_2(goal_focus='insert_edward_2', spatial_focus='object:na location:na direction:na'):
        print('Insert Edward (2)')
        DM.threshold+=.09
        DM.add('object:edward location:0.0 annotation:na')
        spatial_focus.set('object:edward location:0.0 direction:na')
        goal_focus.set('move_right_3')
    
    # 3-construction-move_right
    def move_right_3(goal_focus='move_right_3', spatial_focus='object:edward location:0.0 direction:na'):
        print('Move right (3)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:1.0 direction:right')
        goal_focus.set('insert_derek_4')
    
    # 4-construction-insert_derek
    def insert_derek_4(goal_focus='insert_derek_4', spatial_focus='object:na location:1.0 direction:right'):
        print('Insert Derek (4)')
        DM.threshold+=.09
        DM.add('object:derek location:1.0 annotation:na')
        spatial_focus.set('object:derek location:1.0 direction:right')
        goal_focus.set('read_premise_5')
    
    # 5-construction-read_premise
    def read_premise_5(goal_focus='read_premise_5', spatial_focus='object:derek location:1.0 direction:right'):
        print('Premise two: Derek is to the left of Travis.')
        spatial_focus.set('object:derek location:1.0 direction:right')
        goal_focus.set('move_right_6')
    
    # 6-construction-move_right
    def move_right_6(goal_focus='move_right_6', spatial_focus='object:derek location:1.0 direction:right'):
        print('Move right (6)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.0 direction:right')
        goal_focus.set('insert_travis_7')

    # 7-construction-insert_travis
    def insert_travis_7(goal_focus='insert_travis_7', spatial_focus='object:na location:2.0 direction:right'):
        print('Insert Travis (7)')
        DM.threshold+=.09
        DM.add('object:travis location:2.0 annotation:na')
        spatial_focus.set('object:travis location:2.0 direction:right')
        goal_focus.set('read_premise_8')
    
    # 8-construction-read_premise_8
    def read_premise_8(goal_focus='read_premise_8', spatial_focus='object:travis location:2.0 direction:right'):
        print('Premise three: Travis is to the left of Brian.')
        spatial_focus.set('object:travis location:2.0 direction:right')
        goal_focus.set('move_right_9')
    
    # 9-construction-move_right_9
    def move_right_9(goal_focus='move_right_9', spatial_focus='object:travis location:2.0 direction:right'):
        print('move_right_9')
        DM.threshold+=.09
        spatial_focus.set('object:na location:3.0 direction:right')
        goal_focus.set('insert_brian_10')
    
    # 10-construction-insert_brian_10
    def insert_brian_10(goal_focus='insert_brian_10', spatial_focus='object:na location:3.0 direction:right'):
        print('Insert Brian (10)')
        DM.threshold+=.09
        DM.add('object:brian location:3.0 annotation:na')
        spatial_focus.set('object:brian location:3.0 direction:right')
        goal_focus.set('read_conclusion_11')
    
######---------------------INSPECT-----------------------------#######

    # This function is used to write the conclusions True(1)/False(0) to a csv file
    # FOR /l %i in (1,1,100) DO python 0-2P1D-MMRT.py
    def decision (self,answer):
        myfile=open("XXXXXXX3P1D-thresh-09.csv", "a", newline="")
        wr=csv.writer(myfile)
        wr.writerow(answer)
        myfile.close()


    # 11-inspection-read_conclusion
    def read_conclusion_11(goal_focus='read_conclusion_11', spatial_focus='object:brian location:3.0 direction:right'):
        print('Conclusion: Edward is to the left of Brian. (11)')
        spatial_focus.set('object:brian location:3.0 direction:right')
        goal_focus.set('request_edward_12')
    
    # 12-inspection-request_edward
    def request_edward_12(goal_focus='request_edward_12', spatial_focus='object:brian location:3.0 direction:right'):
        print('Recalling Edward location...(12)')
        DM.request('object:edward location:!3.0')
        spatial_focus.set('object:brian location:3.0 direction:right')
        goal_focus.set('recall_edward_13A1B1C1D1')

##########################################################################################
#--------------------BRANCH-13-A1-B1-C1-D1------------------------------------------------
##########################################################################################

###------------13A1-Recall of Edward location Correct-----------###    

    # 13A1-recall_correct
    def recall_correct_13(goal_focus='recall_edward_13A1B1C1D1', spatial_focus='object:brian location:3.0 direction:right', DMbuffer='location:0.0'):
        print('I recall Edward location to be (0.0) (recall_correct) (13A1)')
        spatial_focus.set('object:brian location:3.0 direction:right')
        goal_focus.set('move_left_13A2')
    
    def move_left_13A2 (goal_focus='move_left_13A2', spatial_focus='object:brian location:3.0 direction:right'):
        print('Move left (13A2)')
        DM.threshold+=.09
        spatial_focus.set('object:travis location:2.0 direction:left')
        goal_focus.set('move_left_13A3')

    def move_left_13A3 (goal_focus='move_left_13A3', spatial_focus='object:travis location:2.0 direction:left'):
        print('Move left (13A3)')
        DM.threshold+=.09
        spatial_focus.set('object:derek location:1.0 direction:left')
        goal_focus.set('move_left_13A4')
    
    def move_left_13A4 (goal_focus='move_left_13A4', spatial_focus='object:derek location:1.0 direction:left'):
        print('Move left (13A4)')
        DM.threshold+=.09
        spatial_focus.set('object:edward location:0.0 direction:left')
        goal_focus.set('confirm_conclusion_13A5')

    def confirm_conclusion_13A5 (goal_focus='confirm_conclusion_13A5', spatial_focus='object:edward location:0.0 direction:left'):
        print('True, Edward is to the left of Brian!  (13A5)')
        self.decision('1')
        self.stop()


###------------13B1-Error of Omission-----------###    

    # 13B1-inspection-recall_omission
    def recall_omission_13B1(goal_focus='recall_edward_13A1B1C1D1', spatial_focus='object:brian location:3.0 direction:right', DM='error:True', DMbuffer=None):
        print('I can not recall Edward location (recall_omission) (13B1)')
        spatial_focus.set('object:brian location:3.0 direction:right')
        goal_focus.set('confirm_conclusion_13B2A1B1')

    # 13B2A1-inspection-confirm_conclusion
    def confirm_conclusion_13B2A1(goal_focus='confirm_conclusion_13B2A1B1', spatial_focus='object:brian location:3.0 direction:right'):
        print('True, Edward is to the left of Brian! (13B2A1)')
        self.decision('1')
        self.stop()
    
    # 13B2B1-inspection-confirm_conclusion
    def confirm_conclusion_13B2B1(goal_focus='confirm_conclusion_13B2A1B1', spatial_focus='object:brian location:3.0 direction:right'):
        print('False, Edward is NOT to the left of Brian! (13B2B1)')
        self.decision('0')
        self.stop()


###------------13C1-Error of Commission...travis-----------###    

    # 13C1-recall_commission...travis
    def recall_commission_13C1 (goal_focus='recall_edward_13A1B1C1D1', spatial_focus='object:brian location:3.0 direction:right', DMbuffer='location:2.0'):
        print('I recall Edward location to be (2.0) (recall_commission...travis) (13C1)')
        spatial_focus.set ('object:brian location:3.0 direction:right')
        goal_focus.set ('move_left_13C2')
    
    # 13C2-move_left
    def move_left_13C2 (goal_focus='move_left_13C2', spatial_focus='object:brian location:3.0 direction:right'):
        print('Move left (13C2)')
        DM.threshold+=.09
        spatial_focus.set('object:travis location:2.0 direction:left')
        goal_focus.set('confirm_conclusion_13C3')
    
    # 13C3-confirm_conclusion
    def confirm_conclusion_13C3 (goal_focus='confirm_conclusion_13C3', spatial_focus='object:travis location:2.0 direction:left'):
        print('True, Edward is to the left of Brian! (13C3)')
        self.decision('1')
        self.stop()


###------------13D1-Error of Commission...derek-----------###    

    # 13D1-recall_commission
    def recall_commission_13D1(goal_focus='recall_edward_13A1B1C1D1', spatial_focus='object:brian location:3.0 direction:right', DMbuffer='location:1.0'):
        print('I recall Edward location to be (1.0) (recall_commission...derek) (13D1)')
        spatial_focus.set('object:brian location:3.0 direction:right')
        goal_focus.set('move_left_13D2')
    
    def move_left_13D2(goal_focus='move_left_13D2', spatial_focus='object:brian location:3.0 direction:right'):
        print('Move left (13D2)')
        DM.threshold+=.09
        spatial_focus.set('object:travis location:2.0 direction:left')
        goal_focus.set('move_left_13D3')
    
    def move_left_13D3(goal_focus='move_left_13D3', spatial_focus='object:travis location:2.0 direction:left'):
        print('Move left (13D3)')
        DM.threshold+=.09
        spatial_focus.set('object:derek location:1.0 direction:left')
        goal_focus.set('confirm_conclusion_13D4')
    
    # 13D4-confirm_conclusion
    def confirm_conclusion_13D4(goal_focus='confirm_conclusion_13D4', spatial_focus='object:derek location:1.0 direction:left'):
        print('True, Edward is to the left of Brian! (13D4)')
        self.decision('1')
        self.stop()


################################################################


nico = MyAgent()
thesis = MyEnvironment()
thesis.agent=nico
python_actr.log_everything(thesis)
thesis.run()
python_actr.finished()

