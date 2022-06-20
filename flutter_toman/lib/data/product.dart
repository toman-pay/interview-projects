class SubmitProductParams {
  final String title;
  final int price;
  final String description;

  SubmitProductParams(
      {required this.title, required this.price, required this.description});
}

class SubmitProductResponse {
  final String message;

  SubmitProductResponse({required this.message});
}
