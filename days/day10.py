input_str = """160
34
123
159
148
93
165
56
179
103
171
44
110
170
147
98
25
37
137
71
5
6
121
28
19
134
18
7
66
90
88
181
89
41
156
46
8
61
124
9
161
72
13
172
111
59
105
51
109
27
152
117
52
68
95
164
116
75
78
180
81
47
104
12
133
175
16
149
135
99
112
38
67
53
153
2
136
113
17
145
106
31
45
169
146
168
26
36
118
62
65
142
130
1
140
84
94
141
122
22
48
102
60
178
127
73
74
87
182
35"""
input_list = list(map(int, input_str.split("\n")))
input_list.append(0)
input_list.append(max(input_list) + 3)
input_list = sorted(input_list)
count = 0
max_adapter = max(input_list)
length = len(input_list)
paths = dict()


def solve1():
    chain = input_list

    ones = 0
    threes = 0
    for el in chain:
        i = chain.index(el)
        if i == 0:
            continue
        last_el = chain[i - 1]
        difference = el - last_el
        if difference == 1:
            ones += 1
        elif difference == 3:
            threes += 1
    print(ones)
    print(threes)
    return ones * threes


def get_available_adapters(adapter):
    adapters = []
    i = input_list.index(adapter)
    if length - i > 1 and input_list[i + 1] - adapter < 4:
        adapters.append(input_list[i + 1])
    if length - i > 2 and input_list[i + 2] - adapter < 4:
        adapters.append(input_list[i + 2])
    if length - i > 3 and input_list[i + 3] - adapter < 4:
        adapters.append(input_list[i + 3])
    return adapters


def solve2():
    for adapter in input_list:
        paths[adapter] = paths.get(adapter, 1)
        adapters = get_available_adapters(adapter)
        for adp in adapters:
            paths[adp] = paths.get(adp, 0) + paths[adapter]
        print(adapter, adapters, paths)

    return paths[max_adapter]
