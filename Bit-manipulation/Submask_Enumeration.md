Given a bitmask  m, you want to efficiently iterate through all of its submasks, that is, masks  
s  in which only bits that were included in mask  m are set.
``` cpp

int s = m;
while (s > 0) {
 cout<<s;
 s = (s-1) & m;
}
cout<<s; // to process submask 0
```

#### Time complexity - O(3^N)

#### Example

| Step  | sub (Current) | sub - 1 | (sub - 1) & 1101 | Resulting Submask (Binary) | Subset of Customers |
|-------|---------------|---------|------------------|----------------------------|---------------------|
| Start | 1101          | -       | -                | 1101                       | {0, 2, 3}           |
| 1     | 1101          | 1100    | 1100 & 1101      | 1100                       | {2, 3}              |
| 2     | 1100          | 1011    | 1011 & 1101      | 1001                       | {0, 3}              |
| 3     | 1001          | 1000    | 1000 & 1101      | 1000                       | {3}                 |
| 4     | 1000          | 0111    | 0111 & 1101      | 0101                       | {0, 2}              |
| 5     | 0101          | 0100    | 0100 & 1101      | 0100                       | {2}                 |
| 6     | 0100          | 0011    | 0011 & 1101      | 0001                       | {0}                 |
| 7     | 0001          | 0000    | 0000 & 1101      | 0000                       | (Loop ends)         |
