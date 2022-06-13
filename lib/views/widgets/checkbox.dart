import 'package:flutter/material.dart';

class TomanCheckbox extends StatefulWidget {
  final Widget title;
  final bool? value;
  final void Function(bool value) onChanged;
  const TomanCheckbox({
    Key? key,
    required this.title,
    required this.value,
    required this.onChanged,
  }) : super(key: key);

  @override
  State<TomanCheckbox> createState() => _TomanCheckboxState();
}

class _TomanCheckboxState extends State<TomanCheckbox> {
  bool _value = false;

  @override
  void initState() {
    if (widget.value != null) {
      _value = widget.value!;
    }
    super.initState();
  }

  @override
  void didUpdateWidget(covariant TomanCheckbox oldWidget) {
    _value = widget.value ?? _value;
    super.didUpdateWidget(oldWidget);
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        setState(() {
          _value = !_value;
        });
        widget.onChanged(_value);
      },
      child: Container(
        color: Colors.transparent,
        child: Row(
          children: [
            Checkbox(
              materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
              value: _value,
              onChanged: (value) {
                setState(() {
                  _value = value ?? false;
                });
                widget.onChanged(_value);
              },
            ),
            widget.title,
          ],
        ),
      ),
    );
  }
}
