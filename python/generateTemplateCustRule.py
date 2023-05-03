

import lorem;
import random;

## *Debit code	*Debit label	*Credit code	*Credit label	*Weight 
(0-100)	Rule description

line = "{debitCode}, {debitLabel}, {creditCode}, {creditLabel}, {weight}, 
{description}"

MAC_CODE = 
[14001,14005,14011,14012,14013,14014,14015,14016,14026,14027,14028,14029,14030,14031,14032,14033,14034,14035,14045,14046,14047,14048,14049,14050,14051,14052,14053,14062,14063,14064,14065,14066,14067,14068,14079,14080,14081,14082,14091,14092,14093,14094,14095,14096,14097,14098,14099,14100,14110,14120,14121,14122,14123,14124,14125,14126,14127,14136,14137,14138,14148,14149,14150,14151,14161,14162,14163,14174,14175,14176,14177,14178,14179,14189,14190,14191,14192,14193,14194,14195,14196,14205,14206,14207,14208,14209,14210,14211,14212,14213,14214,14222,14223,14224,14225,14226,14227,14228,14229,14230,14231,14241,14251,14252,14253,14254,14255,14256,14266,14267,14268,14269,14270,14280,14281,14282,14283,14284,14294,14304,24001,24005,24011,24012,24013,24014,24015,24016,24017,24018,24028,24029,24030,24031,24032,24033,24034,24035,24036,24046,24047,24048,24055,24056,24057,24058,24059,24060,24061,24062,24063,24064,24074,24084,24085,24086,24087,24088,24089,24090,24091,24101,24102,24103,24104,24105,24106,24107,24108,24118,24127,24128,24129,24130,24131,24132,24133,24134,24135,24136,24146,24156,24157,24158,24159,24160,24161,24162,24172,24182,34001,34005,34011,34021,34031,34041,34042,34051,34052,34053,34063,34064,34073,34083,34084,34085,34094,34095,34096,34097,34098,34099,44001,44009,44010,44011,44012,44013,44014,44015,44025,44026,44027,44028,44038,44048,44058,44068,44069,44070,44071,44072,44082,44083,44084,44085,44086,44087,44088,44089,44090,44091,44092,44093,44094,44095,44096,44097,44098,44107,44108,44109,44110,44111,44112,44113,44123,44133,44143,44153,44163,54001,54002,54011,54012,54022,54023,54033,54034,54035,54036,54037,54038,54039,54040,54041,54051,54052,54053,54054,54055,54065,54075,54076,54077,54087,54088,54089,54090,54100,54110,54120,54130,54131,54132,54133,54134,54135,54136,54137,54138,54139,54140,54149,54150,54151,54152,54153,54154,54155,54164,54165,54166,54167,54168,54169,54170,54171,54172,54173,54174,54175,54176,54177,54178,54179,54180,54181,54191,54192,54193,54194,54195,54196,54206,54207,54208,54209,54210,54211,54212,54213,54214,54215,54225,54226,54227,54228,54229,54230,54231,54232,54242,54243,54244,54245,54246,54247,54248,54249,54259,54269,54270,54271,54272,54273,54274,54275,54285,54286,54287,54288,54289,54290,54291,54292,54293,54294,54295,54296,54297,54298,54299,54300,54301,54302,54303,54310,54311,54312,54313,54314,54315,54316,54317,54327,94001,94002,94003,94004,94005,94006,94011,94021]

rows = []
# Setup loop to generate Data 
max = 20
count = 0
while count < max :
    debitCode = random.choice(MAC_CODE)
    debitLabel = lorem.sentence()
    creditCode = random.choice(MAC_CODE)
    creditLabel =lorem.sentence()
    weight = random.randint(0,100)
    description = lorem.sentence();

    line = "{0}, {1}, {2}, {3}, {4}, {5}".format(debitCode,debitLabel, 
creditCode,creditLabel, weight, description)
    rows.append(line)
    count+= 1

print(rows)

# Write output 
