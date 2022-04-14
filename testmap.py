#!/usr/bin/env python

from operator import itemgetter
import sys
import pandas as pd

lines = (",Date,Time,TargetTemp,ActualTemp,System,SystemAge,BuildingID\n"
    "6236,6/27/2013,3:33:07,68,57,1,6,17\n"
    "7567,6/8/2013,0:33:07,70,67,1,12,14\n"
    "3360,6/1/2013,6:13:20,67,67,1,7,9\n"
    "4655,6/6/2013,15:13:19,66,58,1,8,18\n"
    "2377,6/8/2013,21:43:51,67,73,1,11,4\n"
    "7571,6/12/2013,4:33:07,65,71,1,11,14\n"
    "7580,6/21/2013,13:33:07,70,67,1,26,1\n"
    "738,6/19/2013,23:43:51,67,58,1,30,3\n"
    "1487,6/18/2013,9:13:19,69,75,1,8,15\n"
    "338,6/9/2013,2:33:07,69,78,1,15,18\n"
    "7041,6/22/2013,21:33:07,66,79,1,15,15\n"
    "3219,6/10/2013,4:45:56,67,77,1,8,19\n"
    "2385,6/16/2013,5:13:20,66,69,1,9,14\n"
    "6085,6/26/2013,20:43:51,66,60,1,24,8\n"
    "4248,6/19/2013,11:43:51,65,78,1,3,12\n"
    "3673,6/14/2013,7:13:19,67,75,1,24,20\n"
    "744,6/25/2013,5:13:20,66,75,1,15,10\n"
    "4954,6/5/2013,7:13:19,65,61,1,11,8\n"
    "6082,6/23/2013,17:43:51,70,79,1,9,3\n"
    "1862,6/3/2013,5:33:07,67,63,1,14,18\n"
    "1501,6/2/2013,23:13:19,66,78,1,20,11\n"
    "7627,6/8/2013,12:45:56,70,56,1,6,10\n"
    "2204,6/15/2013,16:00:01,70,58,1,27,12\n"
    "1504,6/5/2013,2:43:51,69,55,1,4,11\n"
    "5378,6/9/2013,23:13:20,69,65,1,8,18\n"
    "4951,6/2/2013,4:13:19,67,56,1,29,17\n"
    "4245,6/16/2013,8:43:51,66,73,1,5,8\n"
    "4949,6/30/2013,2:13:19,65,71,1,30,16\n"
    "7063,6/14/2013,19:45:56,65,71,1,3,11\n"
    "2372,6/3/2013,16:43:51,67,56,1,27,9\n"
    "7525,6/26/2013,6:43:51,66,67,1,20,5\n"
    "7526,6/27/2013,7:43:51,66,74,1,6,13\n"
    "2363,6/24/2013,7:43:51,69,60,1,30,13\n"
    "381,6/22/2013,21:00:01,66,56,1,12,17\n"
    "6480,6/1/2013,7:33:07,69,67,1,2,18\n"
    "2812,6/23/2013,5:13:20,66,70,1,5,11\n"
    "5384,6/15/2013,5:33:07,65,73,1,5,18\n"
    "7538,6/9/2013,19:43:51,69,70,1,12,4\n"
    "6133,6/14/2013,20:33:07,66,71,1,3,7\n"
    "1879,6/20/2013,22:33:07,68,64,1,5,15\n"
    "5129,6/30/2013,14:13:20,67,62,1,8,17\n"
    "1169,6/30/2013,3:13:20,68,68,1,30,14\n"
    "717,6/28/2013,2:43:51,67,73,1,21,6\n"
    "4237,6/8/2013,0:43:51,67,75,1,18,8\n"
    "1167,6/28/2013,1:13:20,65,61,1,17,13\n"
    "2215,6/26/2013,3:13:19,66,75,1,30,17\n"
    "3907,6/8/2013,6:13:20,66,67,1,26,20\n"
    "3071,6/12/2013,0:33:07,68,59,1,29,18\n"
    "3697,6/8/2013,7:43:51,65,70,1,20,19\n"
    "4441,6/2/2013,17:43:51,67,65,1,15,11\n"
    "3687,6/28/2013,21:13:19,68,63,1,19,18\n"
    "6102,6/13/2013,13:13:20,67,56,1,22,15\n"
    "1870,6/11/2013,13:33:07,65,68,1,13,2\n"
    "5136,6/7/2013,21:13:20,68,56,1,27,5\n"
    "6100,6/11/2013,11:13:20,67,76,1,5,11\n"
    "3356,6/27/2013,2:13:20,65,56,1,8,16\n"
    "5153,6/24/2013,14:33:07,65,63,1,29,20\n"
    "2030,6/21/2013,5:13:19,65,67,1,9,10\n"
    "753,6/4/2013,14:13:20,70,77,1,12,3\n"
    "4078,6/29/2013,9:00:01,69,75,1,6,20\n"
    "4561,6/2/2013,17:43:51,66,79,1,14,4\n"
    "4072,6/23/2013,3:00:01,67,57,1,25,5\n"
    "268,6/29/2013,4:13:19,70,65,1,14,18\n"
    "2828,6/9/2013,21:13:20,66,69,1,19,7\n"
    "4259,6/30/2013,22:43:51,70,71,1,5,2\n"
    "5175,6/16/2013,12:00:01,68,71,1,19,15\n"
    "6984,6/25/2013,12:43:51,69,65,1,2,7\n"
    "5176,6/17/2013,13:00:01,70,72,1,10,20\n"
    "6552,6/13/2013,7:45:56,65,73,1,30,17\n"
    "6974,6/15/2013,2:43:51,66,63,1,24,3\n"
    "2176,6/17/2013,7:45:56,66,67,1,14,17\n"
    "253,6/14/2013,13:00:01,67,57,1,13,13\n"
    "4408,6/29/2013,8:13:19,65,62,1,12,2\n"
    "251,6/12/2013,11:00:01,65,74,1,30,13\n"
    "6962,6/3/2013,14:13:19,65,68,1,13,7\n"
    "807,6/28/2013,20:00:01,66,62,1,23,15\n"
    "1110,6/1/2013,16:00:01,67,61,1,14,16\n"
    "1836,6/7/2013,3:13:20,67,57,1,28,3\n"
    "2602,6/23/2013,6:43:51,67,80,1,2,3\n"
    "4070,6/21/2013,1:00:01,68,75,1,6,8\n"
    "1102,6/23/2013,8:00:01,70,79,1,10,12\n"
    "2834,6/15/2013,3:33:07,69,68,1,13,14\n"
    "6952,6/23/2013,4:13:19,66,73,1,4,14\n"
    "2936,6/27/2013,9:13:20,65,63,1,27,7\n"
    "784,6/5/2013,21:33:07,65,66,1,10,7\n"
    "7007,6/18/2013,11:13:20,66,70,1,21,14\n"
    "7686,6/7/2013,4:13:19,70,78,1,10,10\n"
    "1126,6/17/2013,8:13:19,70,73,1,29,18\n"
    "7646,6/27/2013,7:45:56,69,80,1,3,2\n"
    "4254,6/25/2013,17:43:51,68,60,1,13,12\n"
    "7031,6/12/2013,11:33:07,70,78,1,13,2\n"
    "3377,6/18/2013,23:13:20,67,70,1,28,19\n"
    "5609,6/30/2013,19:00:01,67,72,1,20,5\n"
    "5157,6/28/2013,18:33:07,65,76,1,22,6\n"
    "5159,6/30/2013,20:33:07,66,58,1,6,20\n"
    "1141,6/2/2013,23:13:19,68,65,1,6,8\n"
    "1139,6/30/2013,21:13:19,65,62,1,24,12\n"
    "763,6/14/2013,0:33:07,69,55,1,23,14\n"
    "3935,6/6/2013,10:33:07,67,61,1,2,12\n"
    "4929,6/10/2013,6:00:01,65,58,1,6,9\n"
    "7524,6/25/2013,5:43:51,65,79,1,7,14\n"
    "765,6/16/2013,2:33:07,67,76,1,2,2\n"
    "4563,6/4/2013,19:43:51,65,77,1,19,19\n"
    "2404,6/5/2013,0:33:07,66,80,1,5,18\n"
    "2759,6/30/2013,0:13:19,65,66,1,2,11\n"
    "6530,6/21/2013,9:45:56,66,56,1,17,19\n"
    "4668,6/19/2013,4:43:51,67,80,1,16,12\n"
    "6026,6/27/2013,9:00:01,70,66,1,18,14\n"
    "3386,6/27/2013,8:33:07,68,64,1,16,14\n"
    "6024,6/25/2013,7:00:01,67,77,1,25,9\n"
    "7680,6/1/2013,22:00:01,65,73,1,11,7\n"
    "6304,6/5/2013,23:13:19,65,75,1,18,7\n"
    "6020,6/21/2013,3:00:01,65,75,1,6,19\n"
    "780,6/1/2013,17:33:07,69,69,1,3,3\n"
    "2612,6/3/2013,16:43:51,66,62,1,20,6\n"
    "6142,6/23/2013,5:00:01,68,61,1,15,5\n"
    "6467,6/18/2013,18:13:20,70,79,1,24,13\n"
    "4498,6/29/2013,2:00:01,69,64,1,23,16\n"
    "5439,6/10/2013,12:45:56,68,72,1,7,6\n"
    "1971,6/22/2013,18:13:20,68,68,1,15,8\n"
    "7228,6/29/2013,21:33:07,66,71,1,3,8\n"
    "4180,6/11/2013,15:33:07,67,57,1,27,20\n"
    "2269,6/20/2013,9:13:20,69,59,1,8,13\n"
    "2268,6/19/2013,8:13:20,68,58,1,24,9\n"
    "612,6/13/2013,17:43:51,65,77,1,14,14\n"
    "4139,6/30/2013,22:43:51,65,55,1,20,5\n"
    "4469,6/30/2013,21:13:20,68,77,1,11,10\n"
    "1264,6/5/2013,2:43:51,70,79,1,15,5\n"
    "5515,6/26/2013,21:13:19,68,64,1,9,12\n"
    "2322,6/13/2013,14:00:01,69,67,1,13,15\n"
    "6383,6/24/2013,6:00:01,66,55,1,27,12\n"
    "1262,6/3/2013,0:43:51,65,59,1,27,12\n"
    "1261,6/2/2013,23:13:19,70,72,1,1,13\n"
    "6388,6/29/2013,11:00:01,68,74,1,2,15\n"
    "2097,6/28/2013,0:33:07,68,79,1,15,3\n"
    "7398,6/19/2013,23:13:19,68,66,1,21,19\n"
    "1980,6/1/2013,3:33:07,67,62,1,7,1\n"
    "625,6/26/2013,6:13:20,69,69,1,13,8\n"
    "6229,6/20/2013,20:13:20,69,79,1,13,20\n"
    "1255,6/26/2013,17:13:19,70,77,1,7,6\n"
    "2261,6/12/2013,1:13:20,69,58,1,11,20\n"
    "5530,6/11/2013,12:43:51,69,77,1,20,1\n"
    "4461,6/22/2013,13:13:20,68,65,1,3,14\n"
    "511,6/2/2013,7:45:56,67,66,1,8,4\n"
    "2999,6/30/2013,0:13:19,65,62,1,7,20\n"
    "597,6/28/2013,2:43:51,67,71,1,2,15\n"
    "1351,6/2/2013,17:00:01,68,63,1,29,1\n"
    "4162,6/23/2013,21:13:20,65,74,1,29,1\n"
    "565,6/26/2013,18:00:01,67,56,1,28,12\n"
    "6294,6/25/2013,13:13:19,66,66,1,28,18\n"
    "7299,6/10/2013,20:43:51,68,63,1,1,14\n"
    "552,6/13/2013,5:00:01,69,63,1,15,16\n"
    "3815,6/6/2013,5:45:56,70,66,1,7,14\n"
    "6289,6/20/2013,8:13:19,67,78,1,3,1\n"
    "6319,6/20/2013,14:43:51,70,59,1,8,1\n"
    "3014,6/15/2013,15:13:19,66,67,1,21,10\n"
    "7310,6/21/2013,7:13:20,65,79,1,16,5\n"
    "2283,6/4/2013,23:13:20,66,80,1,23,4\n"
    "4473,6/4/2013,1:33:07,68,56,1,27,2\n"
    "2779,6/20/2013,20:13:19,68,76,1,13,7\n"
    "5487,6/28/2013,17:00:01,70,57,1,25,20\n"
    "7329,6/10/2013,2:33:07,66,69,1,9,8\n"
    "5497,6/8/2013,3:13:19,66,72,1,28,20\n"
    "2300,6/21/2013,16:33:07,65,80,1,10,18\n"
    "2302,6/23/2013,18:33:07,68,77,1,27,6\n"
    "4171,6/2/2013,6:33:07,66,68,1,30,11\n"
    "1344,6/25/2013,10:00:01,69,65,1,28,12\n"
    "1293,6/4/2013,7:13:20,68,79,1,11,17\n"
    "2307,6/28/2013,23:33:07,66,63,1,8,14\n"
    "3826,6/17/2013,16:45:56,69,58,1,14,9\n"
    "2652,6/13/2013,8:33:07,66,64,1,3,4\n"
    "6361,6/2/2013,8:33:07,69,74,1,25,20\n"
    "7358,6/9/2013,7:00:01,65,77,1,8,15\n"
    "1959,6/10/2013,6:13:20,65,57,1,5,17\n"
    "5360,6/21/2013,5:13:20,66,64,1,7,6\n"
    "2328,6/19/2013,20:00:01,66,55,1,15,13\n"
    "2330,6/21/2013,22:00:01,65,74,1,28,2\n"
    "7137,6/28/2013,2:13:19,68,55,1,24,2\n"
    "6440,6/21/2013,15:43:51,66,71,1,24,8\n"
    "4996,6/17/2013,1:13:20,70,64,1,9,10\n"
    "7129,6/20/2013,18:00:01,68,61,1,15,4\n"
    "1888,6/29/2013,7:00:01,69,75,1,21,20\n"
    "3058,6/29/2013,11:13:20,69,72,1,6,17\n"
    "5397,6/28/2013,18:33:07,65,65,1,18,15\n"
    "3733,6/14/2013,19:13:20,70,80,1,20,19\n"
    "1435,6/26/2013,5:33:07,70,63,1,29,5\n"
    "3890,6/21/2013,13:43:51,70,74,1,24,6\n"
    "7126,6/17/2013,15:00:01,70,55,1,5,2\n"
    "1196,6/27/2013,6:33:07,70,75,1,26,2\n"
    "4219,6/20/2013,6:13:19,66,73,1,5,3\n"
    "4221,6/22/2013,8:13:19,66,63,1,1,18\n"
    "407,6/18/2013,23:13:19,70,59,1,16,10\n"
    "5571,6/22/2013,5:33:07,67,76,1,8,20\n"
    
    "7830,6/1/2013,4:43:51,65,72,11,12,16\n"
    "7927,6/8/2013,5:13:19,65,71,11,23,2\n"
    "3127,6/8/2013,8:13:19,65,62,11,29,12\n"
    "7930,6/11/2013,8:13:19,66,71,11,6,9\n"
    "54,6/25/2013,6:43:51,65,63,11,13,17\n"
    "7222,6/23/2013,15:33:07,66,56,11,29,20\n"
    "2933,6/24/2013,6:13:20,69,66,11,16,12\n"
    "7822,6/23/2013,20:13:19,65,67,11,10,1\n"
    "130,6/11/2013,10:00:01,69,60,11,29,4\n"
    "3600,6/1/2013,6:13:20,67,57,11,16,12\n"
    "3161,6/12/2013,18:43:51,69,74,11,10,20\n"
    "6959,6/30/2013,11:13:19,70,76,11,5,13\n"
    "2913,6/4/2013,10:43:51,70,65,11,1,6\n"
    "7896,6/7/2013,22:33:07,67,58,11,17,5\n"
    "2915,6/6/2013,12:43:51,69,65,11,7,17\n"
    "7294,6/5/2013,15:43:51,69,72,11,22,16\n"
    "3990,6/1/2013,17:13:19,68,62,11,11,19\n"
    "7303,6/14/2013,0:13:20,68,79,11,8,19\n"
    
    "3091,6/2/2013,20:33:07,66,57,13,1,9\n"
    "444,6/25/2013,12:13:20,69,58,13,4,9\n"
    "7352,6/3/2013,1:00:01,69,74,13,19,9\n"
    "4631,6/12/2013,15:00:01,65,63,13,10,17\n"
    "484,6/5/2013,4:45:56,65,78,13,5,5\n"
    "4894,6/5/2013,14:45:56,67,77,13,29,6\n"
    "4855,6/26/2013,23:33:07,65,63,13,10,4\n"
    "2432,6/3/2013,4:00:01,65,76,13,20,7\n"
    "7396,6/17/2013,21:13:19,70,57,13,21,16\n"
    "6223,6/14/2013,14:13:20,67,56,13,17,13\n"
    "488,6/9/2013,8:45:56,69,55,13,15,17\n"
    "7193,6/24/2013,10:13:20,69,57,13,9,6\n"
    "1184,6/15/2013,18:13:20,70,62,13,22,15\n"
    "4856,6/27/2013,0:45:56,66,73,13,23,14\n"
    "1379,6/30/2013,21:13:19,68,76,13,27,4\n"
    "7194,6/25/2013,11:13:20,66,63,13,11,17\n"
    "2440,6/11/2013,12:00:01,70,72,13,5,15\n"
    "4879,6/20/2013,23:45:56,66,58,13,26,20\n"
    "4877,6/18/2013,21:45:56,70,57,13,3,8\n"
    "6232,6/23/2013,23:13:20,70,75,13,13,16\n"
    "6237,6/28/2013,4:33:07,65,62,13,23,2\n"
    
    "7480,6/11/2013,9:00:01,69,65,17,12,14\n"
    "3794,6/15/2013,8:45:56,68,76,17,14,10\n"
    "7597,6/8/2013,6:45:56,66,69,17,11,2\n"
    "3033,6/4/2013,10:43:51,67,57,17,8,18\n"
    "3873,6/4/2013,20:13:19,70,70,17,15,11\n"
    "3309,6/10/2013,3:13:19,67,57,17,6,4\n"
    "7461,6/22/2013,14:33:07,70,80,17,11,16\n"
    "3318,6/19/2013,12:13:19,68,76,17,5,12\n"
    "3322,6/23/2013,16:13:19,67,66,17,5,19\n"
    "7139,6/30/2013,4:13:19,70,57,17,7,18\n"
    "7644,6/25/2013,5:45:56,68,78,17,20,18\n"
    "7649,6/30/2013,10:45:56,68,67,17,21,1\n"
    "1900,6/11/2013,19:00:01,68,74,17,11,1\n"
    "7458,6/19/2013,11:33:07,69,73,17,15,15\n"
    "3040,6/11/2013,17:43:51,70,57,17,6,6\n"
    "293,6/24/2013,5:43:51,67,61,17,7,10\n"
    "7005,6/16/2013,9:13:20,67,78,17,28,17\n"
    "434,6/15/2013,2:13:20,69,67,17,21,16\n"
    "285,6/16/2013,21:13:19,67,58,17,24,15\n"
    
    "5893,6/14/2013,15:43:51,66,56,19,3,17\n"
    "6593,6/24/2013,5:13:19,68,57,19,5,18\n"
    "1620,6/1/2013,22:45:56,68,62,19,11,10\n"
    "2720,6/21/2013,4:45:56,65,70,19,19,17\n"
    "1081,6/2/2013,6:45:56,67,77,19,21,14\n"
    "5168,6/9/2013,5:00:01,68,72,19,12,4\n"
    "4549,6/20/2013,5:43:51,70,61,19,22,9\n"
    "7720,6/11/2013,14:43:51,68,70,19,10,16\n"
    "237,6/28/2013,21:33:07,66,74,19,29,3\n"
    "2194,6/5/2013,6:00:01,68,69,19,30,3\n"
    "3692,6/3/2013,2:43:51,67,65,19,30,9\n"
    "6351,6/22/2013,22:13:20,69,66,19,9,13\n"
    "6879,6/10/2013,3:13:20,69,67,19,8,4\n"
    "892,6/23/2013,9:33:07,67,68,19,4,17\n"
    "4379,6/30/2013,3:00:01,68,57,19,9,4\n"
    "1101,6/22/2013,7:00:01,67,62,19,29,18\n"
    "7637,6/18/2013,22:45:56,65,69,19,3,9\n"
    )

lines = lines.split('\n')
#print(testlines)


import math

temp_cutoff = 2
total_system = 0
total_diff = 0
measured = False

worst_diff = [-1, -1, -1]
worst_sys = [-1, -1, -1]

#print('initial')
lines = lines[1:]
testing_sys = int(lines[0].strip().split(',')[5])
total_system = testing_sys

#print('testing initial system', total_system)

def is_between(time, time_range):
    # if time_range[1] < time_range[0]:
        # return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]

for line in lines:

    #mapper
    
    # print(line)
    # line = line.strip()
    # # split the line into words
    # system_vars = line.split(',')
    # print(system_vars)
    # if len(system_vars) > 1 and system_vars[2].isnumeric():
        # #order_number = system_vars[]
        # timestamp_day = system_vars[0]
        # timestamp_hours = pd.Timestamp(system_vars[1])
        # target_temp = int(system_vars[2])
        # actual_temp = int(system_vars[3])
        # system = int(system_vars[4])
        # age = int(system_vars[5])
        # bldg = int(system_vars[6])
        
        # print('%s\t%s\t%s\t%s\t%s\t%s\t%s', timestamp_day, timestamp_hours, target_temp, actual_temp, system, age, bldg)
    # else:
        # continue
    
        #TODO: actually go through correct stripping/assigning methods
    # remove leading and trailing whitespace
    #line = line.strip()

    # # parse the input we got from mapper.py
    # word, count = line.split('\t', 1)

    # # convert count (currently a string) to int
    # try:
        # count = int(count)
    # except ValueError:
        # # count was not a number, so silently
        # # ignore/discard this line
        # continue
    
    #reducer
    #first attempt stripping
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    system_vars = line.split(',')
    # print(system_vars)
    try:
        if len(system_vars) > 1 and system_vars[3].isnumeric():
            #print('sys vars', system_vars[5])
            #order_number = system_vars[]
            timestamp_day = system_vars[1]
            timestamp_hours = pd.Timestamp(system_vars[2])
            target_temp = int(system_vars[3])
            actual_temp = int(system_vars[4])
            system = int(system_vars[5])
            age = int(system_vars[6])
            bldg = int(system_vars[7])
            
        else:
            #print('continuing off of else')
            continue
            
            
            
    except ValueError as ve:
        # improper usage of vars, so silently
        # ignore/discard this line
        print('value error', ve)
        continue
    
    current_diff = abs(actual_temp - target_temp)
    # print('target temp', target_temp)
    # print('actual temp', actual_temp)
    # print('diff temp', current_diff)
    #print('total sys', total_system, total_diff)
    if current_diff < temp_cutoff:
        current_diff = 0

    #is it below or above temp?
    if target_temp > actual_temp:
        current_diff = current_diff*0.6

    #is it working hours?
    #if timestamp_hours < datetime.time(8) or timestamp_hours > datetime.time(17):
    #df.timestamp.dt.strftime('%H:%M:%S').between('8:00:00','17:00:00')
    #    current_diff = current_diff * 0.2
    

    
    # print(timestamp_hours)
    # print(timestamp_hours.strftime('%H:%M:%S'))
    # print(is_between(timestamp_hours.strftime('%H:%M:%S'), ['08:00:00','17:00:00']))
    
    #go through years in service
    current_diff = current_diff * 1/(1-0.4*age/30)
    if age > 10:
        current_diff = current_diff*age/10
    
    if system == total_system:
        total_diff = total_diff + current_diff
    else:
    
        #print('%s\t%s', total_system, total_diff)

        if total_diff > min(worst_diff):
            
            min_pos = 0
            for i in range(1, len(worst_diff)):
                if worst_diff[i] < worst_diff[min_pos]:
                    min_pos = i
            #print('replacing', min_pos)
            worst_diff[min_pos] = total_diff
            worst_sys[min_pos] = total_system

    total_system = system
    total_diff = current_diff

#print('post')
#print last case
#print('%s\t%s', total_system, total_diff)
if total_diff > min(worst_diff):
    min_pos = 0
    for i in range(1, len(worst_diff)):
        if worst_diff[i] < worst_diff[min_pos]:
            min_pos = i
    worst_diff[min_pos] = total_diff
    worst_sys[min_pos] = total_system

#print worst
print('worst prints')
print('%s\t%s', worst_sys[0], worst_diff[0])
print('%s\t%s', worst_sys[1], worst_diff[1])
print('%s\t%s', worst_sys[2], worst_diff[2])
