public class Question {
  public static boolean isUniqueChars1(String str) {
    if (str.length() > 128) {
        return false;
    }

    boolean[] char_happen = new boolean[128];
    for (int i = 0; i < str.length(); i++) {
      int val = str.charAt(i);
      if (char_happen[val]) {
        return false;
      }
      char_happen[val] = true;
    }
    return true;
  }

  public static boolean isUniqueChars2(String str) {
    if (str.length() > 256) {
      return false;
    }

    int checker = 0;
    for (int i = 0; i < str.length(); i++) {
      int val = str.charAt(i) - 'a';
      if ( (checker & 1 << val) > 0 ) {
        return false;
      }
      checker |= 1 << val;
    }
    return true;
  }

  public static void main(String[] args) {
    String[] words = {"apple", "abcsf", "tennis"};
    for (String word : words) {
      System.out.println(word + ": " + isUniqueChars2(word));
    }
  }
}
