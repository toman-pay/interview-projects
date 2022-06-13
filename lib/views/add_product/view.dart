import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:interview_projects/consts/app_strings.dart';
import 'package:interview_projects/consts/assets.dart';
import 'package:interview_projects/utils/action_sheet.dart';
import 'package:interview_projects/views/add_product/state.dart';
import 'package:interview_projects/views/widgets/button.dart';
import 'package:interview_projects/views/widgets/checkbox.dart';
import 'package:interview_projects/views/widgets/textfield.dart';
import 'package:provider/provider.dart';

class AddProduct extends StatefulWidget {
  const AddProduct({Key? key}) : super(key: key);

  @override
  State<AddProduct> createState() => _AddProductState();
}

class _AddProductState extends State<AddProduct> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    final state = context.read<AddProductState>();
    return Scaffold(
      appBar: AppBar(
        elevation: 1,
        centerTitle: true,
        title: Text(
          'ساخت تراکنش',
          style: Theme.of(context)
              .textTheme
              .bodyText1!
              .copyWith(color: Colors.black),
        ),
        backgroundColor: Theme.of(context).colorScheme.secondary,
      ),
      body: SizedBox(
        height: MediaQuery.of(context).size.height,
        child: Stack(
          children: [
            SingleChildScrollView(
              padding: const EdgeInsets.all(24),
              child: Form(
                key: _formKey,
                child: Column(
                  children: [
                    Row(
                      children: [
                        SvgPicture.asset(Assets.productInfoIcon),
                        const SizedBox(width: 12),
                        const Text('اطلاعات محصول'),
                      ],
                    ),
                    const SizedBox(height: 48),
                    TomanTextField(
                      onChanged: (value) => state.title = value,
                      title: 'عنوان محصول',
                      textInputAction: TextInputAction.next,
                    ),
                    const SizedBox(height: 12),
                    TomanTextField(
                      onChanged: (value) => state.price = value,
                      title: 'قیمت',
                      textInputAction: TextInputAction.next,
                      textInputType: TextInputType.number,
                      suffix: 'تومان',
                      isPrice: true,
                    ),
                    const SizedBox(height: 12),
                    TomanTextField(
                      onChanged: (value) => state.description = value,
                      title: 'توضیحات',
                      textInputAction: TextInputAction.done,
                      maxLines: 3,
                    ),
                    const SizedBox(height: 24),
                    Consumer<AddProductState>(
                      builder: (context, state, child) => TomanCheckbox(
                        title: RichText(
                          textAlign: TextAlign.center,
                          text: TextSpan(
                            style: Theme.of(context).textTheme.bodyText1,
                            children: [
                              TextSpan(
                                text: 'شرایط و قوانین',
                                style: Theme.of(context)
                                    .textTheme
                                    .bodyText2!
                                    .copyWith(
                                        color: Theme.of(context)
                                            .colorScheme
                                            .primary),
                                recognizer: TapGestureRecognizer()
                                  ..onTap = () => _openTermsBottomSheet(state),
                              ),
                              const TextSpan(text: ' را می‌پذیرم.'),
                            ],
                          ),
                        ),
                        value: state.termsAccepted,
                        onChanged: (value) => state.termsAccepted = true,
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Positioned(
              bottom: 16,
              left: 24,
              right: 24,
              child: TomanButton(
                title: 'تایید',
                onPressed: () => _onConfirmed(state),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future<void> _onConfirmed(AddProductState state) async {
    FocusScope.of(context).unfocus();
    if (!state.termsAccepted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          duration: const Duration(seconds: 1),
          content: Text(
            'پذیرش شرایط و قوانین الزامیست.',
            style: Theme.of(context)
                .textTheme
                .bodyText2!
                .copyWith(color: Colors.white),
          ),
          backgroundColor: Colors.red,
        ),
      );
      return;
    }
    ActionSheetUtils.showLoadingIndicator(context);
    final result = await state.addProduct();
    if (mounted) {
      _formKey.currentState?.reset();
      Navigator.of(context).pop();
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          duration: const Duration(seconds: 1),
          content: Text(
            result ? 'عملیات موفق' : 'عملیات ناموفق',
            style: Theme.of(context)
                .textTheme
                .bodyText2!
                .copyWith(color: Colors.white),
          ),
          backgroundColor:
              result ? Theme.of(context).colorScheme.primary : Colors.red,
        ),
      );
    }
  }

  void _openTermsBottomSheet(AddProductState state) {
    FocusScope.of(context).unfocus();
    ActionSheetUtils.showBottomSheet(
      context: context,
      title: 'شرایط و قوانین',
      description: AppStrings.terms,
      buttonTitle: 'شرایط و قوانین را می‌پذیرم',
      onPressed: () {
        Navigator.of(context).pop();
        state.termsAccepted = true;
        state.update();
      },
    );
  }
}
