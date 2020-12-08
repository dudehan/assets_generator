
import 'package:flutter/material.dart';
import 'image_list.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Material App',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Material App Bar'),
        ),
        body: Center(
          child: Builder(
            builder: (ctx) {
              return RaisedButton(
                onPressed: () {
                  Navigator.of(ctx).push(
                    MaterialPageRoute(builder: (ctx) {
                      return ImageList();
                    }),
                  );
                },
                child: Text('图片列表'),
              );
            },
          ),
        )
      ),
    );
  }
}
