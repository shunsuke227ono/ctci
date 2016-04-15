// file to test what i want to test.

final class Hoge {
  int i;
}

class Main {
  static void method1(int[] a) {
    int[] other = { 10 };

    // Java には値渡ししかないため、
    // 引数に直接代入しても呼出し元には影響しない
    a = other;
  }
  static void method2(int[] a) {
    // 参照を値渡ししているため、
    // その参照(ポインタ)が指す先は変更できる
    a[0] = 100;
  }

  static void method3(Hoge h) {
    Hoge other = new Hoge();
    other.i = 10;

    // method1と同様、呼出し元には影響しない
    h = other;
  }
  static void method4(Hoge h) {
    // method2と同様、
    // 参照を値渡ししているため、
    // その参照(ポインタ)が指す先は変更できる
    h.i = 100;
  }

  public static void main(String[] args) {
    int[] array = { 0 };
    System.out.println(array[0]);   // => 0

    method1(array);
    System.out.println(array[0]);   // => 0

    method2(array);
    System.out.println(array[0]);   // => 100

    Hoge hoge = new Hoge();
    System.out.println(hoge.i);   // => 0

    method3(hoge);
    System.out.println(hoge.i);   // => 0

    method4(hoge);
    System.out.println(hoge.i);   // => 100
  }
}

class IntWrapper {
  public int i = 0;
  public IntWrapper() {
  }
}

class Main2 {
  IntWrapper[] array = new IntWrapper[10];

  public Main2() {
    array[0] = new IntWrapper();
  }

  public IntWrapper getFirstInt() {
    return array[0];
  }

  public void incrementFirstInt() {
    IntWrapper first = getFirstInt();
    first.i = first.i + 1;
  }

  public static void main(String[] args) {
    int[] a = new int[]{1,2,3};//①
    int[] b = a;               //②
    b[0] = 5;                  //③
    System.out.println(a[0]);
    int c[] = {3};
    b = c;
    System.out.println(b[0]);
    System.out.println(a[0]);
    b[0] = 4;
    System.out.println(a[0]); // => 2のまま!!
    System.out.println(b[0]); // => 4を返すようになる
    System.out.println(c[0]); // => 4を返すようになる
    Main2 obj = new Main2();
    IntWrapper first = obj.getFirstInt();
    System.out.println(first.i);

    obj.incrementFirstInt();
    System.out.println(first.i);

    obj.incrementFirstInt();
    System.out.println(first.i);
  }
}

class Main3 {
  static int[] array = new int[10];
  static int[] getArray() {
  	return array;
  }
  public static void main(String[] args) {
  	int[] a = getArray();
  	a[0] = 100;
    System.out.println(array[0]);	// => 100
  }
}
