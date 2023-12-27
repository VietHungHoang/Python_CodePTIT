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

## PY02019 - NGUYÊN TỐ CÙNG NHAU
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

## PY02022 - LIỆT KÊ SỐ NGUYÊN TỐ TRONG DÃY
Cho dãy số nguyên dương A[] có N phần tử. Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.           
Các số được liệt kê theo thứ tự xuất hiện.           

**Input:**

* Dòng đầu ghi số N (không quá 500).
* Dòng sau ghi N số của dãy (không quá 6 chữ số).

**Output:**

Ghi ra các số nguyên tố khác nhau trong dãy theo thứ tự xuất hiện và số lần xuất hiện. Mỗi số liệt kê trên 1 dòng.

**Ví dụ:**

**Input**
```
10
2 4 7 5 7 8 9 3 7 2
```
**Output**
```
2 2
7 3
5 1
3 1
```

## PY02023 - SẮP XẾP THEO TỔNG CHỮ SỐ
Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.           
Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.           

**Input:**

* Dòng đầu ghi số bộ test (không quá 10)
* Mỗi bộ test gồm 2 dòng:
* Dòng đầu là số N (N < 100)
* Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.

**Output:**

Với mỗi bộ test, ghi trên một dòng dãy số kết quả.

**Ví dụ:**

**Input**
```
1
8
143 43 22 99 7 9 1111 10000000
```
**Output**
```
10000000 22 1111 7 43 143 9 99
```

## PY02024 - SẮP XẾP THEO TÍCH CHỮ SỐ
Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.           
Hãy sắp xếp dãy số theo tích các chữ số tăng dần. Nếu tích các chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.           

**Input:**

* Dòng đầu ghi số bộ test (không quá 10)
* Mỗi bộ test gồm 2 dòng:
* Dòng đầu là số N (N < 100)
* Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.

**Output:**

Với mỗi bộ test, ghi trên một dòng dãy số kết quả.

**Ví dụ:**

**Input**
```
1
8
143 43 22 99 7 9 1111 10000000
```
**Output**
```
10000000 1111 22 7 9 43 143 99
```

## PY02036 - LIỆT KÊ CẶP SỐ NGUYÊN TỐ CÙNG NHAU
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

## PY02039 - MA TRẬN - 1
Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.           
Với đường chéo chính, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo chính (không tính các phần tử nằm trên đường chéo chính). 

![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/abe349a7-3081-4c5c-9e09-f64e7858380e)

Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy **tổng giá trị các phần tử ở nửa trên** trừ đi **tổng giá trị các phần tử ở nửa dưới**.           
Nhập thêm một giá trị K gọi là *ngưỡng cân đối của ma trận*.  Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.           
Hãy xác định độ chênh lệch và tính cân đối của ma trận.           

**Input:**

* Dòng đầu ghi số N (2 < N < 50)
* N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.
* Dòng cuối ghi số K (0 < K <100)

**Output:**

* Dòng đầu ghi chữ YES hoặc NO
* Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

**Ví dụ:**

**Input**
```
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
```
**Output**
```
YES
3
```

## PY02040 - MA TRẬN - 2
Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.         
Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).           

![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/abe349a7-3081-4c5c-9e09-f64e7858380e)

Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy **tổng giá trị các phần tử ở nửa trên** trừ đi **tổng giá trị các phần tử ở nửa dưới**.           
Nhập thêm một giá trị K gọi là *ngưỡng cân đối của ma trận*.  Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.           
Hãy xác định độ chênh lệch và tính cân đối của ma trận.           

**Input:**

* Dòng đầu ghi số N (2 < N < 50)
* N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.
* Dòng cuối ghi số K (0 < K <100)

**Output:**

* Dòng đầu ghi chữ YES hoặc NO
* Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

**Ví dụ:**

**Input**
```
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
```
**Output**
```
NO
11
```

## ĐOẠN LIÊN TIẾP NHỎ HƠN
Cho dãy số A[] có N phần tử. Với mỗi vị trí thứ i trong dãy, hãy tính độ dài của đoạn liên tiếp tính từ i trở về phía trước mà các giá trị đều nhỏ hơn hoặc bằng A[i].           

**Input: Dòng đầu ghi số bộ test (không quá 10). Mỗi test có 2 dòng.:**

* Dòng đầu tiên gồm 1 số nguyên N (1 ≤ N ≤ 10<sup>5</sup>).
* Dòng tiếp theo gồm N số nguyên A<sub>1</sub>, A<sub>2</sub>, …, A<sub>N</sub> (1 ≤ A[i] ≤ 10<sup>6</sup>).

**Output:**

Với mỗi bộ test, in ra dãy kết quả trên một dòng.

**Ví dụ:**

**Input**
```
1
7
100 80 60 70 60 75 85
```
**Output**
```
1 1 1 2 1 4 6
```

## PY02053 - TÍNH CÂN ĐỐI CỦA MA TRẬN - 2
Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.         
Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).           

![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/abe349a7-3081-4c5c-9e09-f64e7858380e)

Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy **tổng giá trị các phần tử ở nửa trên** trừ đi **tổng giá trị các phần tử ở nửa dưới**.           
Nhập thêm một giá trị K gọi là *ngưỡng cân đối của ma trận*.  Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.           
Hãy xác định độ chênh lệch và tính cân đối của ma trận.           

**Input:**

* Dòng đầu ghi số N (2 < N < 50)
* N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.
* Dòng cuối ghi số K (0 < K <100)

**Output:**

* Dòng đầu ghi chữ YES hoặc NO
* Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

**Ví dụ:**

**Input**
```
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
```
**Output**
```
NO
11
```

## PY02060 - BÀI D. BỘI SỐ CHUNG NHỎ NHẤT
Bội số chung nhỏ nhất của hai số nguyên x và y (viết tắt LCM(x, y)) là số nguyên dương nhỏ nhất chia hết cho cả x và y.  Cho hai số nguyên dương a và b (a ≤ b). Hãy đếm xem có bao nhiêu cặp số nguyên (x, y) sao cho

**LCM(x,y) = a * (a+1) * …. * b**         

**Input:**

Dòng đầu ghi số bộ test (không quá 10).  Mỗi test ghi trên một dòng hai số a và b (a ≤ b ≤ 10<sup>6</sup>)

**Output:**

Với mỗi bộ test, ghi ra số lượng cặp (x, y)  thỏa mãn điều kiện đề bài. Vì kết quả có thể rất lớn nên hãy ghi kết quả theo modulo 10<sup>9</sup> + 7.

**Ví dụ:**

**Input**
```
2
2 3
5 5
```
**Output**
```
9
3
```

## PY02061 - TÍNH TÍCH CHẬP MA TRẬN
Phép tích chập (convolution) là kỹ thuật quan trọng trong xử lý ảnh. Kết quả phép tích chập giữa ma trận x[] và ma trận kernel h[] được xác định bằng công thức: 

![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/1dfb13ab-d91a-4b08-b4f2-d9505c221121)

Trong đó ma trận kernel có kích thước bằng 2k+1. Với kernel 3x3 thì -1 ≤ u,v ≤ 1, do đó, giá trị các phần tử của ma trận kết quả có dạng:    

![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/5ea8c153-64e6-4870-9043-0c9d41ab04c6)

Cho ma trận ảnh và ma trận kernel 3x3. Nhiệm vụ của bạn là hãy thực hiện phép nhân tích chập của 2 ma trận, sau đó tính **tổng tất cả các phần tử của ma trận thu được**.       

![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/467fce15-cac5-4c88-8768-3ecdc82d3766)

Giải thích test: Vị trí ô đầu tiên của ma trận kết quả:     

![image](https://github.com/VietHungHoang/Python_CodePTIT/assets/93313248/36cb98b4-690b-456b-bbf6-89a76a7bdd39)

**Input:**

* Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
* Mỗi test bắt đầu bởi hai số nguyên N và M (3 ≤ N,M ≤ 300).
* Kế tiếp là N dòng, mỗi dòng gồm M số nguyên mô tả ma trận ảnh.
* 3 dòng tiếp theo, mỗi dòng gồm 3 số nguyên mô tả ma trận kernel.
* Giá trị các phần tử của hai ma trận có giá trị tuyệt đối không vượt quá 100.

**Output:**

Với mỗi test, hãy in ra tổng các phần tử của ma trận mới tìm được.

**Ví dụ:**

**Input**
```
2
4 4
2 1 0 0
3 2 1 1
4 3 2 1
2 2 1 0
-1 -1 -1
-1 8 -1
-1 -1 -1
3 3
1 2 3
4 5 6
7 8 9
1 1 1
1 1 1
1 1 1
```
**Output**
```
10
45
```

## PYKT039 - DÃY SỐ PHÙ HỢP
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

## PYKT041 - ĐẾM CẶP ĐỒNG XU
Cho một lưới hình vuông kích thước N*N. Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)). Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.           

**Input:**

* Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)
* N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)

**Output:**

Ghi ra số cặp đồng xu đếm được.

**Ví dụ:**

**Input**
```
4
CC..
C..C
.CC.
.CC.
```
**Output**
```
9
```

## PYKT066 - DÃY CON NGẮN NHẤT
Cho dãy số A[] có N phần tử. Nhiệm vụ của bạn là tìm dãy con liên tiếp có độ dài nhỏ nhất, sao cho Ước số chung lớn nhất của tất cả các phần tử trong dãy đúng bằng K.           

**Input:**

* Dòng đầu tiên là số lượng bộ test T (T <= 10).
* Mỗi test bắt đầu bằng 2 số nguyên N và K.
* Dòng tiếp theo gồm N số nguyên A[i] .
* Giới hạn: 1 <= N <= 1000; 1 <= A[i], K <= 10<sup>9</sup>

**Output:**

Với mỗi test, hãy in ra đáp án trên một dòng. Nếu không tìm được dãy con nào, in ra -1.

**Ví dụ:**

**Input**
```
3
8 3
6 9 7 10 12 24 36 27
4 3
2 4 6 8
4 6
1 2 3 6
```
**Output**
```
2
-1
1
```

## PYKT071 - SỐ KHÔNG GIẢM TRONG FILE NHỊ PHÂN
Cho hai file nhị phân DATA1.in và DATA2.in, mỗi file đều chứa một ArrayList<Integer>. Dữ liệu đảm bảo có không quá 100000 số trong mỗi file, và các số đều nguyên dương, không quá 4 chữ số.           
Một số nguyên dương có từ 2 chữ số trở lên được gọi là không giảm nếu các chữ số từ trái sang phải của nó thỏa mãn không có chữ số đằng sau nào lại nhỏ hơn chữ số phía trước nó. Ví dụ: 899, 1134; 7778.           
Hãy liệt kê các số không giảm xuất hiện trong cả hai file DATA1.in và DATA2.in, các số cần liệt kê theo thứ tự tăng dần và kèm theo số lần xuất hiện trong lần lượt từng file.           

**Input:**

Hai file nhị phân DATA1.in và DATA2.in

**Output:**

Ghi lần lượt từng số thỏa mãn theo thứ tự tăng dần, tiếp theo là số lần xuất hiện trong file 1 rồi đến file 2.

**Ví dụ:**

**Input**
```
Hai file nhị phân
```
**Output**
```
Lần lượt các số thỏa mãn và số lần tương ứng. Ví dụ:
59 1 19
66 6 12
1228 9 10
```

## PYKT072 - XOAY VÒNG XÂU KÝ TỰ
Cho N xâu S[1], S[2], …, S[N] có độ dài bằng nhau. Mỗi bước, với xâu T, bạn được phép xoay vòng 1 kí tự, tức lấy kí tự đầu tiên của T rồi chuyển xuống cuối. Ví dụ xâu “cool” sẽ chuyển thành “oolc”.           
Bạn cần phải xoay N xâu sao cho tất cả chúng đều giống nhau. Hãy xác định số bước ít nhất để hoàn thành được công việc này?           

**Input:**

* Mỗi test bắt đầu bởi số nguyên N (1 ≤ N ≤ 50).
* N dòng tiếp theo, mỗi dòng gồm xâu S[i] có độ dài không quá 50.

**Output:**

Với mỗi test, in ra số bước ít nhất tìm được, nếu không thể biến đổi, hãy in ra “NO”.

**Ví dụ 1:**

**Input**
```
4
xzzwo
zwoxz
zzwox
xzzwo
```
**Output**
```
5
```

**Ví dụ 2:**

**Input**
```
2
molzv
lzvmo
```
**Output**
```
2
```
**Ví dụ 3:**

**Input**
```
3
kc
kc
kc
```
**Output**
```
0
```
**Ví dụ 1:**

**Input**
```
4
xzzwo
zwoxz
zzwox
xzzwo
```
**Output**
```
5
```
**Ví dụ 4:**

**Input**
```
3
aa
aa
ab
```
**Output**
```
-1
```

*Giải thích test 1:* Xoay tất cả các xâu thành “zwoxz”.

## PYKT073 - XÁC ĐỊNH THỂ LOẠI THƠ
Trong thơ ca có rất nhiều các thể thơ và những cách gieo vần khác nhau cho các bài thơ. Trong số những thể thơ đó, bạn có thể lựa chọn cho mình một loại thể thơ riêng để đem lại nhiều hiệu quả cho bài thơ và giúp cho bạn có thể thấy được sự hiệu quả trong cách truyền đạt những cung bậc cảm xúc vào trong bài thơ.           
Cho danh sách các bài thơ gồm hai thể loại thơ lục bát và thơ thất ngôn tứ tuyệt.           
1. Thơ lục bát           
- Là thể thơ dân tộc.           
- Số chữ và số câu: Một cặp hai câu thơ, câu trên sáu chữ (lục), câu dưới tám chữ (bát). Một bài thơ có thể có nhiều cặp lục bát, số lượng cặp câu không hạn định.           
2. Thơ thất ngôn tứ tuyệt           
- Xuất xứ: Trung Quốc           
- Thơ trung đại, thơ cận đại           
- Là bài thơ mà mỗi dòng 7 tiếng, bài có 4 câu (Khai - Thừa - Chuyển - Hợp)           
Nhiệm vụ của bạn là hãy viết chương trình xác định số lượng bài thơ và thể thơ (ghi bằng số) của từng bài từ danh sách các bài thơ có sẵn.           

**Input:**

* Dòng đầu tiên cho số N là tổng số dòng của tất cả các bài thơ.
* N dòng tiếp theo ghi lại các câu thơ của từng bài. Các bài thơ lục bát sẽ đảm bảo không đặt liên tiếp nhau.

**Output:**

In ra kết quả số bài thơ và số tương ứng với thể thơ theo từng dòng.

**Ví dụ:**

**Input**
```
8
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
```
**Output**
```
2
1
2
```

## PYKT074 - GỬI THÔNG BÁO
Một thông báo (notification) là một tin nhắn, thông điệp được hiển thị trong một thời gian ngắn trên thanh trạng thái của thiết bị nhằm gây sự chú ý của người dùng. Nó tương tự như một tin nhắn thông thường (SMS ), tuy nhiên nó khác SMS là dịch vụ này hiện nay là hoàn toàn miễn phí và cần có kết nối internet mới có thể gửi và nhận notification. và notification chỉ có thể gửi cho ứng dụng mà nhà phát triển đã đăng ký và người dùng có cài ứng dụng đó. Các notification này sẽ hiển thị trên thanh trạng thái của smartphone và tablet, thường thanh trạng thái ở phía trên cùng của màn hình. Thông thường một thông báo là được tự động kích hoạt nhằm thông báo tới người dùng là ứng dụng đó đã hoàn thành một công việc nào đó. Hoặc bạn có thể gửi thông tin khuyến mãi tới cho khách hàng của bạn, mời khách hàng tham gia một sự kiện nào đó...           
Theo quy định của một số thiết bị. Nội dung thông báo chỉ được phép chứa tối đa 100 ký tự. Điều này đòi hỏi lập trình viên phải xử lý nội dung các thông báo có độ dài lớn hơn 100 ký tự bằng cách rút gọn thông tin. Tuy nhiên, việc rút gọn phải đảm bảo nguyên tắc không bị cắt giữa từ. Trong trường hợp nếu từ hiện tại làm độ dài thông báo vượt quá 100 ký tự sẽ loại bỏ từ đó khỏi thông báo.           
Nhiệm vụ của bạn là hãy viết chương trình xử lý yêu cầu trên.           

**Input:**

* Dòng đầu tiên là số bộ test T < 100.
* T dòng tiếp theo mỗi dòng là một xâu ký tự có độ dài tối đa 1000 ký tự.

**Output:**

In ra kết quả các thông báo đã xử lý.

**Ví dụ:**

**Input**
```
2
Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
```
**Output**
```
Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va
Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
```







