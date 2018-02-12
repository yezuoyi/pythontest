a = [66.25, 333, 333, 1, 1234.5];
print(a. count(333), a.count(66.25), a.count('x'));
a. insert(2, -1);
a. append(333);
print(a);
print(a. count(333), a.count(66.25), a.count('x'));
a. remove(333);
print(a);
a. reverse();
print(a);
a.sort();
print(a);

stack = [3, 4, 5];
stack. append(6);
stack. append(7);
print(stack);
print(stack.pop());
print(stack);


from collections import deque;
queue = deque(["Eric", "John", " Michael "]);
queue. append("Terry ");
queue. append(" Graham ");
print(queue. popleft());
print(queue. popleft());
print(queue);

vec = [2, 4, 6];
vec1=[3 * x for x in vec];
print(vec1);

vec2 = [[x, x**2] for x in vec];
print(vec2);

freshfruit = ['␣␣ banana ', '␣␣ loganberry ␣', 'passion ␣fruit ␣␣'];
vec3=[weapon . strip() for weapon in freshfruit];
print(vec3);

vec4 = [3 * x for x in vec if x > 3];

print(vec4);

vec5 = [2, 4, 6]
vec6= [4, 3, -9]
vec7=[x * y for x in vec5 for y in vec6]

print(vec7);

vec8=[vec5[i] * vec6[i] for i in range(len(vec5))]

print(vec8);


pi=[str(round(355 / 113, i)) for i in range(1, 6)];

print(pi);

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];
print([[row[i] for row in mat] for i in [0, 1, 2]]);
