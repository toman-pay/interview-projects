import 'package:flutter/material.dart';

class TomanCheckbox extends StatelessWidget {
  final Widget title;
  final bool value;
  final void Function(bool value) onChanged;
  const TomanCheckbox({
    Key? key,
    required this.title,
    required this.value,
    required this.onChanged,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => onChanged(!value),
      child: Container(
        color: Colors.transparent,
        child: Row(
          children: [
            Checkbox(
              materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
              value: value,
              onChanged: (value) => onChanged(value ?? false),
            ),
            title,
          ],
        ),
      ),
    );
  }
}
