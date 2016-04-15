#include<iostream>

class Question
{
public:
  static void reverse(char *str)
  {
    char* end = str;
    char tmp;

    if (str == NULL)
    {
      return;
    }

    // 終端のnull文字時点でストップする
    while (*(end+1))
    {
      ++end;
    }

    // 2つのポインタがで会うまで、
    // ポインタの箇所の値を交換していく
    while (str < end)
    {
      tmp = *str;
      *str = *end;
      *end = tmp;

      ++str;
      --end;
    }
  }

  static int run()
  {
    char input[][10] = { "abcde", "cat" };

    for (int i = 0; i < 2; i++)
    {
      std::cout << "reversing the string: " << input[i] << std::endl;
      reverse(input[i]);
      std::cout << "reverse of input string is " << input[i] << std::endl;
    }

    return 0;
  }
};

int main()
{
  Question::run();
  return 0;
}
