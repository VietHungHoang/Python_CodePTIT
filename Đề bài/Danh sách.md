# DANH SÁCH
## ICPC0101 - THU GỌN DÃY SỐ
Cho dãy số A[] chỉ bao gồm các số nguyên dương. Người ta thu gọn dần dãy số bằng cách loại bỏ các cặp phần tử kề nhau mà có tổng là chẵn. Sau khi cặp phần tử đó bị loại ra thì dãy số được dồn lại. Cứ tiếp tục như vậy cho đến khi không còn cặp phần tử nào kề nhau có tổng chẵn nữa.

Hãy tính xem cuối cùng dãy A[] còn bao nhiêu phần tử.

**Input:**

* Dòng đâu ghi số N là số phần tử của dãy (1 ≤ N ≤ 10<sup>5</sup> tức là dãy A có thể có đến 10 nghìn phần tử).
* Dòng tiếp theo ghi N số của dãy A (1 ≤ A[i] ≤ 100).

**Output:**

Ghi ra trên một dòng số phần tử còn lại trong dãy A[].

**Ví dụ 1:**

**Input**
```
5
2 3 4 5 6
```
**Output**
```
5
```

**Ví dụ 2:**

**Input**
```
10
1 5 5 8 6 4 3 5 9 3
```
**Output**
```
2
```

## ICPC0104 - TÌM SỐ NHỎ NHẤT
Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
* T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤10<sup>5</sup>;
* Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số.

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
12ab29cd19
ab123gh456cd
```
**Output**
```
12
123
```

## ICPC0105 - TÌM SỐ LỚN NHẤT
Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số lớn nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 29.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
* T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤10<sup>5</sup>;
* Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số.

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
12ab29cd19
ab123gh456cd
```
**Output**
```
29
456
```

## ICPC0106 - ĐỔI CƠ SỐ - 2
Cho xâu nhị phân X[] có độ dài n. Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
* T, n, X[] thỏa mãn ràng buộc : 1≤T≤10; 1≤ n≤10<sup>5</sup>; X[i] =0, 1;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
8
10010100010010101
2
10010100010010101
```
**Output**
```
224225
10010100010010101
```
## ICPC0107 - THAY ĐỔI CHỮ SỐ
Cho xâu nhị phân X[] có độ dài n. Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.

**Input:**

* Dòng đầu tiên đưa vào số lượng bộ test T.
* Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test gồm 3 dòng: dòng đầu tiên ghi lại chữ số p và chữ số q; hai dòng kế tiếp ghi lại các số X1 và X2 theo thứ tự.
* T, X1, X2 thỏa mãn ràng buộc: 1≤ T ≤100; 0≤ X1, X2 ≤10<sup>1000</sup>.

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
1
5 6
645 
666
```
**Output**
```
21100 1312
```

## ICPC0108 - SUM TRIPLE ZERO
Cho mảng A[] gồm N số nguyên khác nhau. Nhiệm vụ của bạn là đếm số lượng các bộ ba phần tử khác nhau có tổng là 0. Ví dụ A[] = {0, -1, 2, -3, 1}, ta nhận được kết quả là 2 vì có hai bộ 3: (0, -1, 1) và (2, -3, 1).

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[]; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
* T, N, A[i] thỏa mãn ràng buộc : 1≤T≤100; 1≤ N≤10<sup>3</sup>; -10<sup>9</sup>≤ A[i] ≤10<sup>9</sup>;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
5
0 -1 2 -3 1 
5
1 -2  1  0  5
```
**Output**
```
2
1
```

## ICPC0109 - MIN TRIPLE
Cho mảng A[] gồm N số nguyên.      
Nhiệm vụ của bạn là tìm tổng nhỏ nhất của bộ ba số trong mảng. Ví dụ A[] = {1, 2, 3, 4, 5}, ta nhận được tổng nhỏ nhất của bộ ba số là 1 + 2 + 3 = 6. Chú ý nếu sử dụng kỹ thuật sắp xếp, submit lời giải của bạn sẽ bị fail.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[]; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
* T, N, A[i] thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10<sup>6</sup>; -10<sup>8</sup>≤ A[i] ≤10<sup>8</sup>;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
7
1 2 3 0 -1 8 10 
7
9 8 20 3 4 -1 0
```
**Output**
```
0
2
```

## ICPC0110 - MAX TRIPLE
Cho mảng A[] gồm N số nguyên.      
Nhiệm vụ của bạn là tìm tổng lớn nhất của bộ ba số trong mảng. Chú ý nếu sử dụng kỹ thuật sắp xếp, submit lời giải của bạn sẽ bị fail.      
Ví dụ A[] = {1, 2, 3, 4, 5}, ta nhận được tổng lớn nhất của bộ ba số là 3 + 4 + 5 = 12. 

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[]; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
* T, N, A[i] thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10<sup>6</sup>; -10<sup>8</sup>≤ A[i] ≤10<sup>8</sup>;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
7
1 2 3 0 -1 8 10 
7
9 8 20 3 4 -1 0
```
**Output**
```
21
37
```

## ICPC0111 - XOAY MẢNG
Cho mảng A[] gồm N số nguyên và số tự nhiên d.    Hãy thực hiện quay mảng A[] với d phần tử từ phải qua trái. Ví dụ A[] = {1, 2, 3, 4, 5}, d = 2 ta nhận được mảng A[] = {3, 4, 5, 1, 2}.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[] và số d; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
* T, N, d, A[i] thỏa mãn ràng buộc : 1≤T≤100; 1≤ d≤ N ≤10<sup>7</sup>; 0≤ A[i] ≤10<sup>9</sup>;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
5 2
1 2 3 4 5 
10 3
2 4 6 8 10 12 14 16 18 20
```
**Output**
```
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6
```

## ICPC0112 - PRIME – TRIPLET
Bộ ba số nguyên tố được gọi là Prime- Triplet nếu nó là bộ ba số nguyên tố dưới dạng (p, p +2, p + 6) hoặc (p, p + 4, p+6), trong đó p là một số nguyên tố. Ví dụ các bộ ba số (5, 7, 11) hoặc (7, 11, 13) đều là các Prime-Triplet. Cho số tự nhiên N, nhiệm vụ của bạn là đếm số các Prime-Triplet nhỏ hơn N.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
* T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10<sup>6</sup>;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
15
25
```
**Output**
```
2
5
```

## ICPC0113 - EMIRP NUMBER
Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố, đảo các chữ số của K cũng là một số nguyên tố nhưng không phải chính nó (không đối xứng). Ví dụ số 11 không phải là số Emirp Number. Cho số tự nhiên N, nhiệm vụ của bạn là hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
* T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10<sup>6</sup>;

**Output:**

* Đưa ra kết quả mỗi test theo từng dòng.
* Chú ý: ghi theo các cặp số thỏa mãn từ nhỏ đến lớn, xem ví dụ để hiểu hơn về cách hiển thị kết quả. 

**Ví dụ:**

**Input**
```
2
40
100
```
**Output**
```
13  31
13  31  17  71  37 73 79  97
```

## ICPC0114 - PERFECT PRIME
Một số nguyên dương N được gọi là Perfect Prime nếu N là số nguyên tố; đảo ngược các chữ số của N cũng là một số nguyên tố; tổng các chữ số của N là một số nguyên tố và mỗi chữ số của N cũng là một số nguyên tố. Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không? Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
* T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10<sup>7</sup>;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
3
13
753
757
```
**Output**
```
No
No
Yes
```

## ICPC0115 - SỐ KRISH
Một số nguyên dương N được gọi là số Krish nếu tổng giai thừa các chữ số của N bằng chính nó. Ví dụ N = 145 = 1! + 4! + 5! = 145 là một số Krish. Cho số nguyên dương N, hãy kiểm tra N có phải là một số Krish hay không? Đưa ra “Yes” nếu N là một số Krish, ngược lại đưa ra “No”.

**Input:**

* Dòng đầu tiên đưa vào T là số lượng bộ test.
* Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
* T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N≤10<sup>8</sup>;

**Output:**

Đưa ra kết quả mỗi test theo từng dòng.

**Ví dụ:**

**Input**
```
2
145
235
```
**Output**
```
Yes
No
```

## ICPC0116 - CON SỐ DUYÊN NỢ
Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.       
Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân có chữ số đầu và chữ số cuối giống nhau không?

**Input:**

* Gồm nhiều dòng, mỗi dòng chứa một số nguyên dương n ghi ở hệ thập phân.
* N thỏa mãn ràng buộc : 1≤N≤10<sup>100</sup>;

**Output:**

Ứng với mỗi số nguyên dương n, ghi ra trên một dòng là YES nếu số n tương ứng có chữ số đầu và chữ số cuối giống nhau, NO nếu ngược lại.

**Ví dụ:**

**Input**
```
2
12345
123451
```
**Output**
```
NO
YES
```

## ICPC0117 - CHÚC MỪNG NĂM MỚI
Tí năm nay đã lên lớp 1 rồi, Tết đến Tí rất vui vì nhận được rất nhiều lời chúc.       
Vì mới tập viết nên Tí đã ghi lại tất cả các lời chúc đó. Cũng vì rất trân trọng các lời chúc nên Tí đã ghi tất cả các lời chúc bằng chữ IN HOA, tuy nhiên do mới tập viết nên Tí ghi không có dấu. Giờ ngồi lật lại cuốn nhật ký ghi các lời chúc, Tí thấy mình đã ghi được n lời chúc.        
Tí muốn biết có bao nhiêu lời chúc khác nhau (hai lời chúc được gọi là khác nhau nếu chúng có độ dài khác nhau hoặc tồn tại ít nhất một vị trí mà ký tự ở vị trí đó của hai lời chúc là khác nhau, hay nói cách khác, đó là hai xâu ký tự khác nhau). Bạn hãy lập chương trình giúp Tí đếm xem có bao nhiêu lời chúc khác nhau nhé.

**Input:**

* Dòng đầu chứa số nguyên dương n là số lời chúc Tí ghi được;
* n dòng tiếp theo, mỗi dòng chứa một xâu ký tự S là một lời chúc.
* n, S thỏa mãn ràng buộc: 1 ≤ n ≤ 10^<sup>4</sup>; Các lời chúc S có độ dài không quá 30 ký tự gồm các chữ cái la tinh IN HOA ‘A’…’Z’ và dấu cách.

**Output:**

Một số nguyên dương duy nhất là số lời chúc khác nhau.

**Ví dụ:**

**Input**
```
4
CHUC MUNG NAM MOI
HAPPY NEW YEAR
CHUC MUNG TUOI MOI
CHUC MUNG NAM MOI
```
**Output**
```
3
```

## ICPC0118 - CUNG HOÀNG ĐẠO
Trong chiêm tinh học phương Tây, các cung Hoàng Đạo là mười hai cung 30° của Hoàng Đạo, bắt đầu từ điểm phân Vernal (một trong những giao điểm của Hoàng Đạo với Xích đạo thiên cầu), còn được gọi là Điểm Đầu của Bạch Dương. Thứ tự của các cung Hoàng Đạo là Bạch Dương, Kim Ngưu, Song Tử, Cự Giải, Sư Tử, Xử Nữ, Thiên Bình, Thiên Yết, Nhân Mã, Ma Kết, Bảo Bình và Song Ngư. Mỗi khu vực được đặt tên theo chòm sao mà nó đi qua trong lúc đặt tên. Cung hoàng đạo của một người được xác định dựa trên ngày sinh bằng bảng dưới đây:
![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/a14d3f53-2d46-46f6-970a-29631710712e)

Ví dụ: nếu sinh nhật của một người là vào ngày 5 tháng 5, thì họ là Kim Ngưu, vì nó nằm trong khoảng từ ngày 21 tháng 4 đến ngày 20 tháng 5.      
Nhiệm vụ của bạn là xác định cung hoàng đạo của một ngày sinh bất kỳ.

**Input:**

* Dòng đầu tiên đưa vào số lượng bộ test T.
* Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test gồm 2 số cách nhau bởi một khoảng trống d và m, trong đó d là ngày, m là tháng.

**Output:**

Đưa ra cung hoàng đạo dựa vào bảng đã cho tương ứng với ngày tháng nhập vào.

**Ví dụ:**

**Input**
```
2
5 5
30 7
```
**Output**
```
Kim Nguu
Su Tu
```

## PY02002 - LIỆT SỐ FIBONACCI
Dãy số Fibonacci được định nghĩa theo công thức như sau:

* F<sub>1</sub> = 1
* F<sub>2</sub> = 1
* F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> với n>2

Cho hai số nguyên dương a và b (1 < a < b < 93). Viết chương trình liệt kê các số Fibonacci từ a đến b.

**Input:**

* Dòng đầu ghi số bộ test, không quá 10.
* Mỗi bộ test viết trên một dòng hai số a và b.

**Output:**

Ghi ra kết quả của mỗi test trên một dòng, mỗi số cách nhau một khoảng trống.

**Ví dụ:**

**Input**
```
1
1 10
```
**Output**
```
1 1 2 3 5 8 13 21 34 55
```

## PY02003 - DÃY SỐ HAMMING
Dãy số nguyên dương tăng dần trong đó ước số nguyên tố lớn nhất của các số trong dãy đều không vượt quá 5 được gọi là dãy số Hamming. Ví dụ 10 = 2x5 thuộc dãy Hamming còn 26 = 2x13 không thuộc dãy Hamming.       
Số 1 được coi là số đầu tiên của dãy Hamming.           
Cho số nguyên dương N.  Hãy xác định xem N có thuộc dãy Hamming hay không và nếu có thì thứ tự của N trong dãy Hamming là bao nhiêu.
**Input:**

* Dòng đầu tiên ghi số bộ test (không quá 105).
* Mỗi test ghi một số N (1 ≤ N ≤ 10<sup>18</sup>).

**Output:**

* Nếu giá trị N thuộc dãy Hamming thì ghi ra thứ tự của N (tính từ 1).
* Nếu không thì ghi ra “Not in sequence”

**Ví dụ:**

**Input**
```
11
1
2
6
7
8
9
10
11
12
13
14
```
**Output**
```
1
2
6
Not in sequence
7
8
9
Not in sequence
10
Not in sequence
Not in sequence
```

## PY02004 - DÃY SỐ NHỊ PHÂN
Cho dãy số A[] chỉ có các giá trị nhị phân 0 và 1.          
Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.

**Input:**

* Dòng 1 ghi số N là số phần tử của dãy (không quá 100).
* Dòng 2 ghi N số nhị phân.

**Output:**

Ghi ra kết quả bài toán.

**Ví dụ:**

**Input**
```
6
1 0 0 1 1 1
```
**Output**
```
2
```

## PY02005 - CẶP NGHỊCH THẾ
Cho dãy số A[] gồm có N phần tử.           
Một cặp nghịch thế là một cặp số (u, v) sao cho u < v và A[u] > A[v]. Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A[] ban đầu.           

**Input:**

* Dòng đầu tiên là N (N ≤ 1000), số lượng phần tử trong dãy số ban đầu.
* Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 10<sup>9</sup>).

**Output:**

In ra một số nguyên là số lượng dãy nghịch thế tìm được.

**Ví dụ:**

**Input**
```
5
2 4 1 3 5
```
**Output**
```
3
```

*Giải thích test:*

Có 3 cặp nghịch thế là (2, 1), (4,1) và (4, 3).

## PY02006 - DÃY SỐ PHÙ HỢP
Cho hai dãy số A[] và B[] có cùng N phần tử. Dãy số A[] được gọi là phù hợp với dãy số B[] khi và chỉ khi tồn tại một phép sắp đặt lại các phần tử trong A[] và B[] sao cho phần tử thứ i của A[] nhỏ hơn hoặc bằng phần tử thứ i của mảng B[] (với tất cả vị trí trong dãy).           
Hãy xác định hai dãy số A[] và B[] có phù hợp với nhau hay không?           

**Input:**

* Dòng đầu tiên đưa vào số lượng bộ test T (T≤100).
* Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm 3 phần: phần thứ nhất là số N; phần thứ hai là N số của A[]; phần thứ 3 là N số của B[].
* (1≤N≤100, 0≤A[i], B[i]≤1000)

**Output:**

Đưa ra kết quả mỗi test theo từng dòng. Kết quả “YES” nếu A[] phù hợp với B[], ngược lại đưa ra “NO”.

**Ví dụ:**

**Input**
```
2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84
```
**Output**
```
YES
NO
```

## PY02007 - CHIA DƯ CHO 42
Cho dãy số A có 10 phần tử là các số nguyên dương. Hãy đếm xem sẽ có bao nhiêu số khác nhau trong dãy nếu tất cả các phần tử đều được chia dư cho 42.           

**Input:**

Gồm 10 số nguyên dương, viết trên một hoặc nhiều dòng.

**Output:**

Ghi ra các số khác nhau tìm được sau khi đã chia dư cho 42.

**Ví dụ 1:**

**Input**
```
1 2 3 4 5 6  7 8  9 10
```
**Output**
```
10
```

**Ví dụ 2:**

**Input**
```
42 84 252 420 840
126 42 84 420 126
```
**Output**
```
1
```

**Ví dụ 3:**

**Input**
```
39 40 41 42 43 44 82
83 84 85
```
**Output**
```
6
```

## PY02008 - KHOẢNG CÁCH NGUYÊN TỐ
Cho hai số nguyên N và X.           
Bắt đầu từ số X, hãy liệt kê N +1 số liên tiếp sao cho khoảng cách giữa số trước và số sau lần lượt là các số trong dãy N số nguyên tố đầu tiên.           
Ví dụ N=5 và X=4. Vì 5 số nguyên tố đầu tiên là 2 3 5 7 11 nên ta có 6 số trong dãy cần liệt kê là: 4 6 9 14 21 32           

**Input:**

Chỉ có 1 dòng ghi 2 số N và X. (2 ≤ N ≤ 1000; 1 ≤ X ≤ 100)

**Output:**

Ghi ra trên một dòng lần lượt N+1 số của dãy kết quả.

**Ví dụ:**

**Input**
```
5 4
```
**Output**
```
4 6 9 14 21 32
```

## PY02009 - TRÚNG THƯỞNG
Chung kết Euro 2020, quá nhiều người dự đoán đúng Italia thắng Anh bằng đá luân lưu 11m. Ban tổ chức chương trình Dự đoán tỉ số trúng Mercedes thấy rất khó trao giải nên quyết định tìm người được trao thưởng bằng cách chạy đoạn code lựa chọn ngẫu nhiên.      
Các người chơi dự đoán đúng được đánh số thứ tự bắt đầu từ 1, giả sử cũng có không quá 1000 người. Chương trình sẽ thực hiện lấy ngẫu nhiên N lần, mỗi lần 1 giá trị từ 1 đến 1000, N cũng không quá 1000.           
Sau khi kết thúc N lần ngẫu nhiên, con số nào được chọn nhiều lần nhất sẽ cho biết người trúng thưởng. Trong trường hợp có nhiều số có số lần xuất hiện bằng nhau và lớn nhất thì số có giá trị nhỏ nhất sẽ được chọn.           
Hãy giúp BTC tìm ra người được trao thưởng.           

**Input:**

* Dòng đầu ghi số bộ test, không quá 100.
* Mỗi bộ test gồm N+1 dòng. Dòng đầu ghi số N. Tiếp theo là N dòng ghi các giá trị ngẫu nhiên nhận được.

**Output:**

Với mỗi test, ghi ra số thứ tự của người được trao thưởng.

**Ví dụ:**

**Input**
```
3
3
999
999
19
4
13
333
333
13
3
11
12
13
```
**Output**
```
999
13
11
```

## PY02013 - BIẾN ĐỔI VỀ 1
Cho số nguyên dương N. Mỗi bước thực hiện các phép biến đổi N theo quy tắc sau           
* Nếu N chẵn thì N = N/2           
* Nếu N lẻ thì N = N*3 + 1           
Hãy đếm xem có bao nhiêu giá trị xuất hiện cho đến khi N = 1. Tất nhiên nếu ban đầu N = 1 thì chỉ có một giá trị duy nhất.           
Ví dụ: N = 3 thì sẽ có 8 giá trị xuất hiện lần lượt là: 3, 10, 5, 16, 8, 4, 2, 1           

**Input:**

* Có nhiều test, mỗi test ghi trên một dòng số nguyên dương N  không quá 100.
* Input kết thúc khi N = 0.

**Output:**

Với mỗi test, ghi ra kết quả tính được trên một dòng.

**Ví dụ:**

**Input**
```
1
2
3
0
```
**Output**
```
1
2
8
```

## PY02015 - BIẾN ĐỔI DÃY SỐ
Cho một dãy số A[] có 4 số nguyên dương, đánh số vị trí từ 1 đến 4. Tại mỗi bước, giá trị A[i] được thay thế bằng abs(A[i] – A[i+1]), riêng A[4] = abs(A[4]-A[1]).           
Hàm abs (trị tuyệt đối) được sử dụng để đảm bảo các giá trị của dãy số luôn dương.           
Hãy đếm xem sau bao nhiêu bước thì dãy số A[] có cả 4 vị trí đều bằng nhau.           

**Input:**

Có 4 số của dãy A[], các giá trị không quá 9 chữ số. Input kết thúc với 4 số 0.

**Output:**

Với mỗi test, ghi ra số bước cần thực hiện.

**Ví dụ:**

**Input**
```
1 3 5 9
4 3 2 1
0 0 0 0
```
**Output**
```
6
4
```

## PY02016 - XUẤT HIỆN NHIỀU LẦN NHẤT
Cho dãy số A[] gồm có N phần tử. Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.           

**Input:**

* Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
* Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu.
* Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 1 000 000).

**Output:**

* Với mỗi test in ra đáp án của bài toán trên một dòng. Nếu có nhiều số cùng có tần số xuất hiện nhiều nhất như nhau và đều thỏa mãn số lần lớn hơn N/2 thì in ra số nhỏ nhất.
* Nếu không tìm được đáp án, in ra “NO”.

**Ví dụ:**

**Input**
```
2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4
```
**Output**
```
4
NO
```

## PY02018 - SỐ NHỎ NHẤT CÒN THIẾU
Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau. Hãy tìm số nhỏ nhất còn thiếu trong dãy số đó.           

**Input:**

* Dòng đầu ghi số N (1 <= N <= 30000).
* Dòng tiếp theo ghi N số của dãy A (1 <= A[i] <= 30000).

**Output:**

Ghi ra số nhỏ nhất còn thiếu nếu có (khi dãy số đầy đủ các số từ 1 đến N thì số nhỏ nhất còn thiếu sẽ là N+1).

**Ví dụ:**

**Input**
```
3
1 2 4
```
**Output**
```
3
```

## PY 02019 - NGUYÊN TỐ CÙNG NHAU
Cho dãy số A[] có n phần tử là các số nguyên dương khác nhau, giá trị không quá 100. Hãy liệt kê các cặp số nguyên tố cùng nhau xuất hiện trong dãy theo thứ tự tăng dần, mỗi cặp số in trên một dòng.           
Một cặp số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng 1.           

**Input:**

* Dòng đầu ghi số n (không quá 100).
* Dòng thứ 2 ghi n số của dãy A[]

**Output:**

Ghi lần lượt các cặp số nguyên tố cùng nhau theo thứ tự tăng dần.

**Ví dụ:**

**Input**
```
5
3 7 9 6 13
```
**Output**
```
3 7
3 13
6 7
6 13
7 9
7 13
9 13
```

## PY02020 - TÍNH ĐIỂM TRUNG BÌNH
Sau khi xem Olympic Tokyo 2020, Nam nhận thấy ở một số nội dung thi có chấm điểm thì điểm được tính cho vận động viên sẽ bỏ qua các giá trị điểm thấp nhất và cao nhất sau đó mới tính trung bình.           
Nam mở rộng bài toán như sau: Có N giám khảo, mỗi giám khảo cho một giá trị điểm là một số thực trong đoạn từ 0 đến 10. Hãy loại bỏ các giá trị điểm bằng với điểm thấp nhất hoặc cao nhất, sau đó in ra điểm trung bình của các giá trị còn lại.           
Dữ liệu vào của bài toán đảm bảo luôn có ít nhất 3 giá trị khác nhau trong các giá trị điểm ban đầu.           

**Input:**

* Dòng đầu ghi số N là số giám khảo (không quá 100).
* Dòng thứ 2 ghi N giá trị điểm, là các số thực trong đoạn [0,10] - đảm bảo luôn có ít nhất 3 giá trị khác nhau.

**Output:**

Ghi ra giá trị điểm trung bình sau khi đã loại bỏ các giá trị nhỏ nhất và lớn nhất. Kết quả được ghi với đúng 2 số phần thập phân.

**Ví dụ:**

**Input**
```
6
6.75 8 9.2 7.25 7.75 6.75
```
**Output**
```
7.67
```










