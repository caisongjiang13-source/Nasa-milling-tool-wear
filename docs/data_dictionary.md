# NASA Milling Data Dictionary

| 字段 | 它代表什么 | 单位 |
| --- | --- | --- |
| VB        | 后刀面磨损  | mm |
| DOC       | 切削深度    | mm |
| feed      | 进给量      | mm/rev |
| material  | 材料编号    | 1-cast iron, 2-steel |
| time      | 时间相关数据| 待核对 |

sample rate = 250 Hz

In the same case, DOC & feed & material are the same

mill(0-16) : case 1
mill(17-30) : case 2
mill(31-44) : case 3
mill(45-51) : case 4
mill(52-60) : case 9
mill(61-70) : case 10
mill(71-93) : case 11
mill(94-108) : case 12
mill(109-114) : case 5
mill(115-115) : case 6
mill(116-123) : case 7
mill(124-129) : case 8
mill(130-144) : case 13
mill(145-153) : case 14
mill(154-160) : case 15
mill(161-166) : case 16

0 case= 1 run= 1 VB= 0
1 case= 1 run= 2 VB= nan
2 case= 1 run= 3 VB= nan
# 3 case= 1 run= 4 VB= 0.11
4 case= 1 run= 5 VB= nan
5 case= 1 run= 6 VB= 0.2
6 case= 1 run= 7 VB= 0.24
7 case= 1 run= 8 VB= 0.29
# 8 case= 1 run= 9 VB= 0.28
9 case= 1 run= 10 VB= 0.29
10 case= 1 run= 11 VB= 0.38
11 case= 1 run= 12 VB= 0.4
12 case= 1 run= 13 VB= 0.43
# 13 case= 1 run= 14 VB= 0.45
14 case= 1 run= 15 VB= 0.5
15 case= 1 run= 16 VB= nan
16 case= 1 run= 17 VB= 0.44
17 case= 2 run= 1 VB= 0.08
18 case= 2 run= 2 VB= 0.14
19 case= 2 run= 3 VB= 0.14
20 case= 2 run= 4 VB= 0.14
21 case= 2 run= 5 VB= 0.15
22 case= 2 run= 6 VB= nan
23 case= 2 run= 7 VB= 0.18
24 case= 2 run= 8 VB= 0.22
25 case= 2 run= 9 VB= 0.26
26 case= 2 run= 10 VB= 0.31
27 case= 2 run= 11 VB= 0.38
28 case= 2 run= 12 VB= 0.43
29 case= 2 run= 13 VB= 0.48
30 case= 2 run= 14 VB= 0.55
31 case= 3 run= 1 VB= 0
32 case= 3 run= 2 VB= 0.13
33 case= 3 run= 3 VB= 0.13
34 case= 3 run= 5 VB= 0.17
35 case= 3 run= 6 VB= 0.19
36 case= 3 run= 7 VB= 0.2
37 case= 3 run= 8 VB= 0.23
38 case= 3 run= 9 VB= 0.23
39 case= 3 run= 10 VB= 0.26
40 case= 3 run= 11 VB= 0.28
41 case= 3 run= 12 VB= 0.33
42 case= 3 run= 14 VB= 0.36
43 case= 3 run= 15 VB= 0.44
44 case= 3 run= 16 VB= 0.55
45 case= 4 run= 1 VB= 0.08
46 case= 4 run= 2 VB= 0.13
47 case= 4 run= 3 VB= 0.2
48 case= 4 run= 4 VB= 0.31
49 case= 4 run= 5 VB= 0.35
50 case= 4 run= 6 VB= 0.4
51 case= 4 run= 7 VB= 0.49
52 case= 9 run= 1 VB= 0
53 case= 9 run= 2 VB= 0.1
54 case= 9 run= 3 VB= 0.14
55 case= 9 run= 4 VB= 0.19
56 case= 9 run= 5 VB= 0.27
57 case= 9 run= 6 VB= 0.38
58 case= 9 run= 7 VB= 0.47
59 case= 9 run= 8 VB= 0.64
60 case= 9 run= 9 VB= 0.81
61 case= 10 run= 1 VB= 0
62 case= 10 run= 2 VB= 0.04
63 case= 10 run= 3 VB= 0.08
64 case= 10 run= 4 VB= 0.16
65 case= 10 run= 5 VB= 0.25
66 case= 10 run= 6 VB= 0.36
67 case= 10 run= 7 VB= 0.43
68 case= 10 run= 8 VB= 0.47
69 case= 10 run= 9 VB= 0.53
70 case= 10 run= 10 VB= 0.7
71 case= 11 run= 1 VB= 0
72 case= 11 run= 2 VB= 0.04
73 case= 11 run= 3 VB= 0.07
74 case= 11 run= 4 VB= 0.07
75 case= 11 run= 5 VB= 0.08
76 case= 11 run= 6 VB= 0.09
77 case= 11 run= 7 VB= nan
78 case= 11 run= 8 VB= 0.12
79 case= 11 run= 9 VB= 0.16
80 case= 11 run= 10 VB= 0.18
81 case= 11 run= 11 VB= 0.2
82 case= 11 run= 12 VB= 0.23
83 case= 11 run= 13 VB= 0.26
84 case= 11 run= 14 VB= nan
85 case= 11 run= 15 VB= 0.31
86 case= 11 run= 16 VB= 0.37
87 case= 11 run= 17 VB= nan
88 case= 11 run= 18 VB= 0.42
89 case= 11 run= 19 VB= 0.47
90 case= 11 run= 20 VB= 0.57
91 case= 11 run= 21 VB= 0.65
92 case= 11 run= 22 VB= 0.68
93 case= 11 run= 23 VB= 0.76
94 case= 12 run= 1 VB= nan
95 case= 12 run= 2 VB= 0.05
96 case= 12 run= 3 VB= 0.08
97 case= 12 run= 4 VB= nan
98 case= 12 run= 5 VB= 0.12
99 case= 12 run= 6 VB= 0.17
100 case= 12 run= 7 VB= 0.2
101 case= 12 run= 8 VB= 0.24
102 case= 12 run= 9 VB= 0.32
103 case= 12 run= 10 VB= nan
104 case= 12 run= 11 VB= 0.4
105 case= 12 run= 12 VB= 0.45
106 case= 12 run= 13 VB= 0.49
107 case= 12 run= 14 VB= 0.58
108 case= 12 run= 15 VB= 0.65
109 case= 5 run= 1 VB= 0
110 case= 5 run= 2 VB= 0.16
111 case= 5 run= 3 VB= 0.29
112 case= 5 run= 4 VB= 0.44
113 case= 5 run= 5 VB= 0.53
114 case= 5 run= 6 VB= 0.74
115 case= 6 run= 1 VB= 0
116 case= 7 run= 1 VB= 0
117 case= 7 run= 2 VB= 0.09
118 case= 7 run= 3 VB= 0.13
119 case= 7 run= 4 VB= 0.22
120 case= 7 run= 5 VB= 0.24
121 case= 7 run= 6 VB= 0.34
122 case= 7 run= 7 VB= 0.46
123 case= 7 run= 8 VB= nan
124 case= 8 run= 1 VB= 0
125 case= 8 run= 2 VB= 0.18
126 case= 8 run= 3 VB= 0.3
127 case= 8 run= 4 VB= nan
128 case= 8 run= 5 VB= 0.44
129 case= 8 run= 6 VB= 0.62
130 case= 13 run= 1 VB= nan
131 case= 13 run= 2 VB= nan
132 case= 13 run= 3 VB= 0.1
133 case= 13 run= 4 VB= 0.13
134 case= 13 run= 5 VB= 0.17
135 case= 13 run= 6 VB= 0.32
136 case= 13 run= 7 VB= 0.38
137 case= 13 run= 8 VB= 0.49
138 case= 13 run= 9 VB= 0.56
139 case= 13 run= 10 VB= 0.68
140 case= 13 run= 11 VB= 0.83
141 case= 13 run= 12 VB= 0.92
142 case= 13 run= 13 VB= 1.07
143 case= 13 run= 14 VB= 1.3
144 case= 13 run= 15 VB= 1.53
145 case= 14 run= 1 VB= nan
146 case= 14 run= 2 VB= 0.09
147 case= 14 run= 3 VB= 0.17
148 case= 14 run= 4 VB= 0.24
149 case= 14 run= 5 VB= nan
150 case= 14 run= 6 VB= 0.35
151 case= 14 run= 8 VB= 0.6
152 case= 14 run= 9 VB= 0.81
153 case= 14 run= 10 VB= 1.14
154 case= 15 run= 1 VB= nan
155 case= 15 run= 2 VB= 0.15
156 case= 15 run= 3 VB= 0.28
157 case= 15 run= 4 VB= 0.37
158 case= 15 run= 5 VB= 0.48
159 case= 15 run= 6 VB= 0.56
160 case= 15 run= 7 VB= 0.7
161 case= 16 run= 1 VB= nan
162 case= 16 run= 2 VB= nan
163 case= 16 run= 3 VB= 0.24
164 case= 16 run= 4 VB= nan
165 case= 16 run= 5 VB= 0.4
166 case= 16 run= 6 VB= 0.62