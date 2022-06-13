import 'package:flutter/material.dart';
import 'package:interview_projects/confg/design.dart';
import 'package:interview_projects/confg/theme.dart';
import 'package:interview_projects/utils/number.dart';

class TomanTextField extends StatefulWidget {
  final String title;
  final void Function(String value) onChanged;
  final bool obscureText;
  final TextInputAction? textInputAction;
  final TextInputType? textInputType;
  final String? suffix;
  final int? maxLines;
  final bool isPrice;
  const TomanTextField({
    Key? key,
    required this.onChanged,
    required this.title,
    this.obscureText = false,
    this.textInputAction,
    this.textInputType,
    this.suffix,
    this.maxLines,
    this.isPrice = false,
  }) : super(key: key);

  @override
  State<TomanTextField> createState() => _TomanTextFieldState();
}

class _TomanTextFieldState extends State<TomanTextField> {
  final _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(widget.title),
        const SizedBox(height: 8),
        SizedBox(
          height: widget.maxLines == null || widget.maxLines == 1 ? 48 : null,
          child: TextFormField(
            onChanged: _onChanged,
            maxLines: widget.maxLines,
            obscureText: widget.obscureText,
            obscuringCharacter: '*',
            textInputAction: widget.textInputAction,
            keyboardType: widget.textInputType,
            decoration: InputDecoration(
              contentPadding:
                  const EdgeInsets.only(bottom: 4, right: 12, left: 12),
              suffixText: widget.suffix,
              enabledBorder: OutlineInputBorder(
                borderRadius: DesignConfig.mediumBorderRadius,
                borderSide: BorderSide(
                  color: Theme.of(context).colorScheme.grey,
                ),
              ),
              focusedBorder: OutlineInputBorder(
                borderRadius: DesignConfig.mediumBorderRadius,
                borderSide: BorderSide(
                  color: Theme.of(context).colorScheme.primary,
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }

  void _onChanged(value) {
    if (widget.isPrice) {
      _onPriceChanged(value);
      return;
    }
    widget.onChanged(value);
  }

  void _onPriceChanged(String value) {
    String formatted = NumberUtils.priceFormat(value);
    _controller.value = TextEditingValue(
      text: formatted,
      selection: TextSelection.collapsed(offset: formatted.length),
    );
    widget.onChanged(value.replaceAll(',', ''));
  }
}
