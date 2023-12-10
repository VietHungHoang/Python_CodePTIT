# DANH SÁCH
## ICPI0101 - THU GỌN DÃY SỐ
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

## ICPI0104 - TÌM SỐ NHỎ NHẤT
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

## ICPI0105 - TÌM SỐ LỚN NHẤT
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

## ICPI0106 - ĐỔI CƠ SỐ - 2
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
## ICPI0107 - THAY ĐỔI CHỮ SỐ
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
21100  1312
```

## ICPI0108 - SUM TRIPLE ZERO
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

## ICPI0109 - MIN TRIPLE
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

## ICPI0110 - MAX TRIPLE
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

## ICPI0111 - XOAY MẢNG
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

## ICPI0112 - PRIME – TRIPLET
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

## ICPI0113 - EMIRP NUMBER
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

## ICPI0114 - PERFECT PRIME
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

## ICPI0115 - SỐ KRISH
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

## ICPI0116 - CON SỐ DUYÊN NỢ
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

## ICPI0117 - CHÚC MỪNG NĂM MỚI
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

## ICPI0118 - CUNG HOÀNG ĐẠO
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







