import python_actr   
from python_actr import *
import csv

#------------------------------------------------------ 

### PROBLEM #36 MMRT ###

# P1) Edward is below and to the left of Derek.
# P2) Derek is below and to the left of Travis.
# C) EDWARD IS BELOW AND TO THE LEFT OF TRAVIS.


# Relation: Spatial
# Premise: Two
# Dimensions: Two
# Answer: True
# Solution: True
# Premise Order: Continuous
# CPhrasing: Afirst

# Avg_Acc: 0.8125
# Avg_RT: 27.92271635

# Accumulated number of moves for spatial focus construction : 11

# C:\Users\turca\Documents\2-coding_projects\5-ICCM-pyv310\python_actr-main> FOR /l %i in (1,1,310) DO python 02-2P2D_MMRT.py

# FOR 5
# FOR /l %i in (1,1,2170) DO python 02-2P2D_ICCM.py

# FOR 10
# FOR /l %i in (1,1,3100) DO python 02-2P2D_ICCM.py

# FOR 30
# FOR /l %i in (1,1,10000) DO python 02-2P2D_ICCM.py

# ------------------------------------------------------

class MyEnvironment(python_actr.Model):
    pass


class MyAgent(ACTR):

    spatial_focus=Buffer()
    goal_focus=Buffer()
    DMbuffer=Buffer()

    production_time=0.05
    production_sd=0.05
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

    partial.similarity('derek','travis', 0)


#####-----------------------CONSTRUCTION-------------------------------------#####

    goal_focus.set('read_premise_1')
    spatial_focus.set('object:na location:na direction:na')

    # 1-construction-read_premise
    def read_premise_1(goal_focus='read_premise_1', spatial_focus='object:na location:na direction:na'):
        print('Premise 1: Edward is below and to the left of Derek. (1)')
        spatial_focus.set('object:na location:0.0 direction:na')
        goal_focus.set('insert_edward_2')

    # 2-construction-insert_edward
    def insert_edward_2(goal_focus='insert_edward_2' , spatial_focus='object:na location:0.0 direction:na'):
        print('Insert Edward (2)')
        DM.threshold+=.09
        DM.add('object:edward location:0.0 annotation:na')
        spatial_focus.set('object:edward location:0.0 direction:na')
        goal_focus.set('move_above_3')

    # 3-construction-move_above
    def move_above_3(goal_focus='move_above_3', spatial_focus='object:edward location:0.0 direction:na'):
        print('Move above (3)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:0.1 direction:above')
        goal_focus.set('move_right_4')

    # 4-construction-move_right
    def move_right_4(goal_focus='move_right_4', spatial_focus='object:na location:0.1 direction:above'):
        print('Move right (4)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:1.1 direction:right')
        goal_focus.set('insert_derek_5')

    # 5-construction-insert_derek
    def insert_derek_5(goal_focus='insert_derek_5', spatial_focus='object:na location:1.1 direction:right'):
        print('Insert Derek (5)')
        DM.threshold+=.09
        DM.add('object:derek location:1.1 annotation:na')
        spatial_focus.set('object:derek location:1.1 direction:right')
        goal_focus.set('read_premise_6')


    # 6-construction-read_premise
    def read_premise_6(goal_focus='read_premise_6', spatial_focus='object:derek location:1.1 direction:right'):
        print('Premise 2: Derek is below and to the left of Travis.')
        spatial_focus.set('object:derek location:1.1 direction:right')
        goal_focus.set('move_above_7')

    # 7-construction-move_above
    def move_above_7(goal_focus='move_above_7', spatial_focus='object:derek location:1.1 direction:right'):
        print('Move above (7)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:1.2 direction:above')
        goal_focus.set('move_right_8')

    # 8-construction-move_right
    def move_right_8(goal_focus='move_right_8', spatial_focus='object:na location:1.2 direction:above'):
        print('Move right (8)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.2 direction:right')
        goal_focus.set('insert_travis_9')

    # 9-construction-insert_travis
    def insert_travis_9(goal_focus='insert_travis_9', spatial_focus='object:na location:2.2 direction:right'):
        print('Insert Travis (9)')
        DM.threshold+=.09
        DM.add('object:travis location:2.2 annotation:na')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('read_conclusion_10')



######---------------------INSPECT-----------------------------#######

    # This function is used to write the conclusions True(1)/False(0) to a csv file
    # FOR /l %i in (1,1,100) DO python 03-2P2D_MMRT.py
    def decision (self,answer):
        myfile=open("2P2D-thresh-09.csv", "a", newline="")
        wr=csv.writer(myfile)
        wr.writerow(answer)
        myfile.close()

    #10-inspection-read_conclusion
    def read_conclusion_10(goal_focus='read_conclusion_10',spatial_focus='object:travis location:2.2 direction:right'):
        print('Conclusion: Edward is below and to the left of Travis (10).')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('request_edward_11')
    
    #11-inspection-request_edward
    def request_edward_11(goal_focus='request_edward_11', spatial_focus='object:travis location:2.2 direction:right'):
        print('I am recalling Edward location...(11)')
        DM.request('object:edward location:!2.2')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('recall_edward_12A1B1C1')
    
##########################################################################################
#--------------------BRANCH-12-A1-B1-C1------------------------------------------------
##########################################################################################

###------------12A1-Recall of Edward location Correct-----------###    

    #12A1-inspection-recall_correct
    def recall_correct_12A1(goal_focus='recall_edward_12A1B1C1', spatial_focus='object:travis location:2.2 direction:right', DMbuffer='location:0.0'):
        print('I recall Edward location to be (0.0) (recall_correct) (12A1)')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('move_below_12A2')
    
    #12A2-inspection-move_below
    def move_below_12A2(goal_focus='move_below_12A2', spatial_focus='object:travis location:2.2 direction:right'):
        print('Move below (12A2)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.1 direction:below')
        goal_focus.set('move_left_12A3')
    
    #12A3-inspection-move_left
    def move_left_12A3(goal_focus='move_left_12A3', spatial_focus='object:na location:2.1 direction:below'):
        print('Move left (12A3)')
        DM.threshold+=.09
        spatial_focus.set('object:derek location:1.1 direction:left')
        goal_focus.set('move_below_12A4')

    #12A4-inspection-move_below
    def move_below_12A4(goal_focus='move_below_12A4', spatial_focus='object:derek location:1.1 direction:left'):
        print('Move below (12A4)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:1.0 direction:below')
        goal_focus.set('move_left_12A5')
    
    #12A5-inspection-move_left
    def move_left_12A5(goal_focus='move_left_12A5', spatial_focus='object:na location:1.0 direction:below'):
        print('Move left (12A5)')
        DM.threshold+=.09
        spatial_focus.set('object:edward location:0.0 direction:left')
        goal_focus.set('confirm_conclusion_12A6')
    
    #12A6-inspection-confirm_conclusion
    def confirm_conclusion_12A6(goal_focus='confirm_conclusion_12A6', spatial_focus='object:edward location:0.0 direction:left'):
        print('True, Edward is below and to the left of Travis! (12A6) (recall_correct)')
        self.decision('1')
        self.stop()

################################################################################################

###-------12B1-Error of Omission-------------####

    #12B1-inspection-recall_omission
    def recall_omission_12B1(goal_focus='recall_edward_12A1B1C1', spatial_focus='object:travis location:2.2 direction:right', DM='error:True', DMbuffer=None):
        print('I can not recall Edward location (12B1)')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('confirm_conclusion_12B2A1B1')

    #12B2A1-inspection-confirm_conclusion
    def confirm_conclusion_12B2A1(goal_focus='confirm_conclusion_12B2A1B1', spatial_focus='object:travis location:2.2 direction:right'):
        print('True, Edward is below and to the left of Travis! (12B2A1) (recall_omission)')
        self.decision('1')
        self.stop()
    
    #12B2B1-inspection-confirm_conclusion
    def confirm_conclusion_12B2B1(goal_focus='confirm_conclusion_12B2A1B1', spatial_focus='object:travis location:2.2 direction:right'):
        print('False, Edward is NOT below and to the left of Travis! (12B2B1) (recall_omission)')
        self.decision('0')
        self.stop()
    



################################################################################################

###-------12C1-Error of Commission-------------####

    #12C1-recall_commission...derek
    def recall_commission_12C1(goal_focus='recall_edward_12A1B1C1', spatial_focus='object:travis location:2.2 direction:right', DMbuffer='location:1.1'):
        print('I recall Edward to be at location (1.1) (recall_commission) (12C1)')
        spatial_focus.set('object:travis location:2.2 direction:right')
        goal_focus.set('move_below_12C2')
    
    #12C2-move_below
    def move_below_12C2(goal_focus='move_below_12C2', spatial_focus='object:travis location:2.2 direction:right'):
        print('Move below (12C2)')
        DM.threshold+=.09
        spatial_focus.set('object:na location:2.1 direction:below')
        goal_focus.set('move_left_12C3')
    
    #12C3-move_left
    def move_left_12C3(goal_focus='move_left_12C3', spatial_focus='object:na location:2.1 direction:below'):
        print('Move left (12C3)')
        DM.threshold+=.09
        spatial_focus.set('object:derek location:1.1 direction:left')
        goal_focus.set('confirm_conclusion_12C4')
    
    #12C4-confirm_conclusion
    def confirm_conclusion_12C4(goal_focus='confirm_conclusion_12C4', spatial_focus='object:derek location:1.1 direction:left'):
        print('True, Edward is below and to the left of Travis! (12C4) (recall_commission)')
        self.decision('1')
        self.stop()
    

################################################################


nico = MyAgent()
thesis = MyEnvironment()
thesis.agent=nico
python_actr.log_everything(thesis)
thesis.run()
python_actr.finished()

