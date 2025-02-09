# MetalCutplan
for find the quantity of the metal profile you need to buy to finish the job.

## the project text is base on Thai language 

there are still have some bug left. but willbe fix in late version

how to use

1. click crate `1 Mem` for 1 box (each box can calculate 1 metal profile)  or put interger number in box and click `Create` to create multiple box (you can click `1Mem` Multiple times for multiple box too )
2. In `Main` box, For`รูปทรงโลหะ` select metal profile from the drop down list. For `ความยาวเต็มเส้น(MAX)` is maximum length in meter unit of the metal profile you have to buy (normally is 6) `**the number nedd to be integer`, finally select the meatl type from `ชนิดโลหะ`
3. Then the next box will appear. for the `Size` box  fill the empty text box with your profile detail such as height ,width and thickness in `milimeter` unit. (`Hbeam,Chanel` have2 thickness thickness1 is middle section of the profile thickness 2 is the fin part)
4. Next focus on  the `Set quantity` box, fill the text box with interger number for how many length of the part you have to use then click `Add All` . for example in format  " length: quantity " the requirement is 5:2 , 3:1 , 0.75:3 , 2.5:3 that mean you have 4 length  (5,3,0.75,2.5) that have to be set.
also you can click `Add1` to crate 1 empty entry or click `Delete1` to delete 1 entry ,in case you crate too many entry.

5. `for Calculateion` will appear,now fill them with length and quantity that you need. the `left entry is for length` the number can be decimal or interger number but couldn't be greater than maximum length in `ความยาวเต็มเส้น(MAX)` and `right is for quantity` number can only be interger number. **All entry have to be fill otherwise the program will get an error.
6.  back to the `Result` box and click `Calculate`button.
7.  the number after `ต้องสั้งซื้อ` is quntity you hav e to purchase ,`พื้นที่ผิวรวม` is surface area and `นน.รวม` is total weight of you require metal.

