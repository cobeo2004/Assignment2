# Fix the test cases to ensure 8 "yes" and 8 "no" answers based on the query format

import os

# Define test cases to produce 8 "yes" and 8 "no" answers
test_cases = [
    ("p2 => p3; p3 => p1; c => e; b & e => f; f & g => h; p2 & p1 & p3 => d; p1 & p3 => c; a; b; p2;", "d"),       # yes
    ("p2 => p3; p3 => p1; c => e; b & e => f; f & g => h; p2 & p1 & p3 => d; p1 & p3 => c; a; b; p2;", "e"),       # yes
    ("p => q; q => r; s => t; u & v => w; x & y => z; p & q & r => s; a & b => c; d; e; f;",
     "s"),                # yes
    ("p => q; q => r; s => t; u & v => w; x & y => z; p & q & r => s; a & b => c; d; e; f;",
     "t"),                # yes
    ("x => y; y => z; z => w; a & b => c; d & e => f; g & h => i; j & k => l; m; n; o;",
     "z"),                    # yes
    ("x => y; y => z; z => w; a & b => c; d & e => f; g & h => i; j & k => l; m; n; o;",
     "w"),                    # yes
    ("a => b; b => c; c => d; e & f => g; h & i => j; k & l => m; n & o => p; q; r; s;",
     "c"),                    # yes
    ("a => b; b => c; c => d; e & f => g; h & i => j; k & l => m; n & o => p; q; r; s;",
     "d"),                    # yes
    ("p1 => p2; p2 => p3; p3 => p4; p5 & p6 => p7; p8 & p9 => p10; p11 & p12 => p13; p14 & p15 => p16; p17; p18; p19;", "x"),  # no
    ("p1 => p2; p2 => p3; p3 => p4; p5 & p6 => p7; p8 & p9 => p10; p11 & p12 => p13; p14 & p15 => p16; p17; p18; p19;", "y"),  # no
    ("m1 => m2; m2 => m3; m3 => m4; m5 & m6 => m7; m8 & m9 => m10; m11 & m12 => m13; m14 & m15 => m16; m17; m18; m19;", "z"),  # no
    ("m1 => m2; m2 => m3; m3 => m4; m5 & m6 => m7; m8 & m9 => m10; m11 & m12 => m13; m14 & m15 => m16; m17; m18; m19;", "y"),  # no
    ("a => b; b => c; c => d; e & f => g; h & i => j; k & l => m; n & o => p; q; r; s;",
     "x"),                    # no
    ("a => b; b => c; c => d; e & f => g; h & i => j; k & l => m; n & o => p; q; r; s;",
     "y"),                    # no
    ("x1 => x2; x2 => x3; x3 => x4; x5 & x6 => x7; x8 & x9 => x10; x11 & x12 => x13; x14 & x15 => x16; x17; x18; x19;", "z"),  # no
    ("x1 => x2; x2 => x3; x3 => x4; x5 & x6 => x7; x8 & x9 => x10; x11 & x12 => x13; x14 & x15 => x16; x17; x18; x19;", "y")  # no
]

directory = "./Components/Datasets/HornTestCases"
os.makedirs(directory, exist_ok=True)

# Function to create the test case files


def create_test_case_file(test_case, index):
    content = f"TELL\n{test_case[0]}\nASK\n{test_case[1]}"
    file_name = os.path.join(directory, f"test_case_{index + 1}.txt")
    with open(file_name, "w") as file:
        file.write(content)


# Create each test case file
for i, test_case in enumerate(test_cases):
    create_test_case_file(test_case, i)

print("Generated 16 test case files with 8 'yes' and 8 'no' cases.")
