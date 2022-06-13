import 'package:interview_projects/providers/core.dart';
import 'package:interview_projects/services/network/request.dart';
import 'package:interview_projects/services/network/requst_helper.dart';

class AddProductState extends CoreProvider {
  String title = '';
  String price = '';
  String description = '';
  bool termsAccepted = false;

  Future<bool> addProduct() async {
    final service = RequestService(
      RequestHelper.addProduct,
      body: {
        'title': title,
        'description': description,
        'price': price,
      },
    );
    await service.post();
    return service.isSuccess;
  }
}
