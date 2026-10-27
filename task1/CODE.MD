# University Scholarship Allocation System

## 1. Problem Statement

Design a Python program to allocate university scholarships based on students' aggregate marks, subject-wise minimum marks, attendance percentage, and family annual income. The program checks eligibility, ranks eligible students according to aggregate marks, and resolves ties using predefined rules such as higher attendance and lower family income.

## 2. Algorithm

1. Start the program.
2. Read the number of students.
3. Enter each student's name, aggregate marks, subject marks, attendance percentage, and annual family income.
4. Check the eligibility conditions:
   - Aggregate marks ≥ 75%.
   - Each subject mark ≥ 40%.
   - Attendance ≥ 75%.
   - Annual family income ≤ ₹2,50,000.
5. Separate eligible and ineligible students.
6. Rank eligible students by:
   - Higher aggregate marks first.
   - Higher attendance if aggregate marks are equal.
   - Lower family income if both are equal.
   - Student name in alphabetical order if all previous criteria are equal.
7. Display the ranked eligible students and ineligible students.
8. Stop.

Note: These are example scholarship rules for this program. Actual university scholarship criteria may differ.

## 3. Flowchart


## 4. Python Source Code

```
students = []n = int(input("Enter number of students: "))for i in range(n):    print("\nEnter details of student", i + 1)    name = input("Name: ")    aggregate = float(input("Aggregate marks (%): "))    print("Enter marks of 3 subjects:")    s1 = float(input("Subject 1: "))    s2 = float(input("Subject 2: "))    s3 = float(input("Subject 3: "))    attendance = float(input("Attendance (%): "))    income = float(input("Annual family income (Rs.): "))    eligible = (        aggregate >= 75 and        min(s1, s2, s3) >= 40 and        attendance >= 75 and        income <= 250000    )    if eligible:        students.append({            "name": name,            "aggregate": aggregate,            "attendance": attendance,            "income": income        })# Rank by aggregate, attendance, income, then namestudents.sort(
```

## 5. Sample Input

```
Enter number of students: 3

Enter details of student 1
Name: Ravi
Aggregate marks (%): 85
Subject 1: 80
Subject 2: 90
Subject 3: 75
Attendance (%): 90
Annual family income (Rs.): 200000

Enter details of student 2
Name: Sita
Aggregate marks (%): 85
Subject 1: 80
Subject 2: 90
Subject 3: 85
Attendance (%): 95
Annual family income (Rs.): 150000

Enter details of student 3
Name: Arun
Aggregate marks (%): 72
Subject 1: 70
Subject 2: 65
Subject 3: 75
Attendance (%): 80
Annual family income (Rs.): 180000
```

## 6. Sample Output

```
--- SCHOLARSHIP RANK LIST ---
1 Sita | Aggregate: 85.0 | Attendance: 95.0 | Income: 150000.0
2 Ravi | Aggregate: 85.0 | Attendance: 90.0 | Income: 200000.0

Total eligible students: 2
```

Explanation: Sita gets Rank 1 because both Sita and Ravi have 85% aggregate marks, but Sita has higher attendance. Arun is ineligible because his aggregate marks are below 75%.

## 7. Mermaid Flowchart Code

Copy this code into the [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_bd\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_bd\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_bd\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_bd\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_bd\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_bd\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_bd\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_bd\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_bd\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_bd\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bd\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bd\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_bd\_ p{margin:0;}#chatgpt-mermaid-\_r_bd\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_bd\_ .label text,#chatgpt-mermaid-\_r_bd\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ .node rect,#chatgpt-mermaid-\_r_bd\_ .node circle,#chatgpt-mermaid-\_r_bd\_ .node ellipse,#chatgpt-mermaid-\_r_bd\_ .node polygon,#chatgpt-mermaid-\_r_bd\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ .rough-node .label text,#chatgpt-mermaid-\_r_bd\_ .node .label text,#chatgpt-mermaid-\_r_bd\_ .image-shape .label,#chatgpt-mermaid-\_r_bd\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_bd\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ .rough-node .label,#chatgpt-mermaid-\_r_bd\_ .node .label,#chatgpt-mermaid-\_r_bd\_ .image-shape .label,#chatgpt-mermaid-\_r_bd\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_bd\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_bd\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bd\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bd\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_bd\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_bd\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_bd\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_bd\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_bd\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_bd\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_bd\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_bd\_ .icon-shape,#chatgpt-mermaid-\_r_bd\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_bd\_ .icon-shape p,#chatgpt-mermaid-\_r_bd\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_bd\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_bd\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_bd\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_bd\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_bd\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_bd\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_bd\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_bd\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_bd\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bd\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_bd\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bd\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_bd\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_bd\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_bd\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_bd\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ .node rect,#chatgpt-mermaid-\_r_bd\_ .node circle,#chatgpt-mermaid-\_r_bd\_ .node ellipse,#chatgpt-mermaid-\_r_bd\_ .node polygon,#chatgpt-mermaid-\_r_bd\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_bd\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_bd\_ .node.mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_bd\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_bd\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_bd\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of studentsEnter student detailsAggregate = 75?Mark as IneligibleAll subject marks = 40?Attendance = 75%?Income <= 250000?Add to Eligible ListMore students?Sort by Aggregate,Attendance, Income and NameDisplay Ranked EligibleStudentsStopNoYesNoYesNoYesNoYesYesNo

Result: The Python program evaluates scholarship eligibility, ranks eligible students, and resolves ties using the specified rules.

