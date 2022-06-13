class NumberUtils {
  static String priceFormat(String number) {
    String price = number
        .replaceAll(RegExp(r'\D'), '')
        .replaceAll(RegExp(r'\B(?=(\d{3})+(?!\d))'), ',');
    return price;
  }
}
