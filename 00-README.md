# python_actr
- A Python implementation of the ACT-R cognitive Architecture using PRISM to model questions of the MRRT.
- use pyv310.8

MODELS AND THEIR MOVES

PRISMS four moves of it's spatial focus, followd by the alternative names used for the MMRT tasks. 
- move forward == move above
- move backwards == move below
- move left == move left
- move right == move right

ACT-R productions will be named after the above convention as well as :
- read_premise
- read_conclusion
- insert_name
- request_name
- correct_recall
- error_omission
- error_commission
- conclusion_true
- conclusion_false

For all names place an '_number' afterwards so as to not call the same production / chunk value - these numbers are not meaningful. 

All productions should be commented with an alphanumeric organization so as to show how the branching of logic operated on these
tasks - these numbers are meaningful. 
   


# --------------------------------------------------------------------------
SUB-SYMBOLIC PARAMETER VALUES

- production_time = 0.05
- production_sd = 0.01
- production_threhold = -20

