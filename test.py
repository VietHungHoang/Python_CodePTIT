file = open("DATA.in", "r", encoding='utf-8')
l = []
for line in file:
    if line.strip() != "":
        l.append(line.strip())
l.remove(l[1])
out = open("data.txt", "w", encoding='utf-8')
out.write("## " + l[0] + "\n")
l.remove(l[0])
i = 0

while not l[i].startswith("Input"):
    out.write(l[i] + "           \n")
    i += 1
if not l[i].endswith(":"): l[i] = l[i] + ":"
out.write("\n**" + l[i] + "**\n\n")
i += 1
tmp = []
while not l[i].startswith("Output"):
    tmp.append(l[i])
    i += 1

if len(tmp) > 1:
    for j in range(len(tmp)):
        out.write("* " + tmp[j] + "\n")
else: out.write(tmp[0] + "\n")

if not l[i].endswith(":"): l[i] = l[i] + ":"
out.write("\n**" + l[i] + "**\n\n")
i += 1

tmp.clear()
while not l[i].startswith("Ví dụ"):
    tmp.append(l[i])
    i += 1

if len(tmp) > 1:
    for j in range(len(tmp)):
        out.write("* " + tmp[j] + "\n")
else: out.write(tmp[0] + "\n")

if not l[i].endswith(":"): l[i] = l[i] + ":"
out.write("\n**" + l[i] + "**\n")
i += 3
out.write("\n**Input**\n")
out.write("```\n")
n = int(input())
for j in range(n):
    out.write(l[i] + "\n")
    i += 1
out.write("```")
out.write("\n**Output**\n")
out.write("```\n")
while i < len(l) - 1:
    out.write(l[i] + "\n")
    i += 1
out.write(l[-1] + "\n```\n\n")