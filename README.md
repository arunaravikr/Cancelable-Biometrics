<h1>A Fingerprint Based Novel Cancelable Biometric Authentication Technique</h1>

<h2>Aim</h2>
● To safeguard biometric data stored in the database.<br>
● To generate a cancelable biometric template without compromising the performance
of the system.<br>
● To generate a non-invertible biometric template, to prevent attackers in generating
original data.<br>
● To be able to authenticate a slightly distorted biometric input.<br>
● To make a user friendly and secured authentication and authorization system.<br>

<h2>Tech Used</h2>
● Python Version 2.7

<h2>Steps to Execute the Project</h2>


1. To Implement this Python 2.7 was Used. <br><br>
```Install Python 2.7 from Python Official Website```

<br>

2. Preprocessing Technique execution takes place through this command which will be output 3 Images. <br><br>
```python mextract.py images/karthik.bmp 1 16 --smooth --save```

<br>

3. Run the <b>fvs2.py</b> file which generates hashes to compare the Candidate and Original Minutaes. <br><br>
```python fvs2.py```
  
<br>
  
 4. Final Run the <b>main.py</b> file which compares the Fingerprint images and generates Average Similarity Value to Determine if the Fingerprint Match was a True Positive or True Negative <br><br>
```python main.py input/karthik.bmp```
  
<br>


