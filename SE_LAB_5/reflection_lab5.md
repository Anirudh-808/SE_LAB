1.Which issues were the easiest to fix, and which were the hardest? Why?

I found the changing the default value of 'history' into None and using the 'with' clause to be the easiest
fixes as i easily understood the need for them and how to implement the fix, meanwhile, changing eval to int
and catching specific exceptions were as easy to identify

2.Did the static analysis tools report any false positives? If so, describe one example.

The analysis tool did not flag the fact that the load_meter_data() function did not close the file
after use, which is a major concern.

3.How would you integrate static analysis tools into your actual software development workflow?

These analysis tools would be useful to analyse code at both intermediate and final
stages to identify and rectify bugs or mistakes before execution or even testing, and
can also be used for improving code readability in case of pylint.

4.What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Upon using the int() change from eval(), I could immediately see that it now
checked for valid values, improving security. The biggest obvious change was in
code readability after applying pylint changes in spacing, removing trailing
whitespaces, etc.