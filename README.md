1. 给定一段html，内容如下
```html
<table border="1">
	<thead>
		<tr>
			<td>name</td>
			<td>age</td>
			<td>operate</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>user0</td>
			<td>18</td>
			<td><input type="button" value="delete" /></td>
		</tr>
	</tbody>
</table>
```

给定一个文件data.json，内容如下
```json
[
  {
    "name": "user1",
    "age": 18
  },
  {
    "name": "user2",
    "age": 18
  }
]
```

请用任意语言实现ajax请求该json文件，将数据插入表格(并增加第三列删除按钮)，并实现delete按钮删除本行的功能。

2. 给定日志文件a.log，内容格式如下
```text
2018-01-01 12:20:24 "SELECT * FROM table1;"
2018-01-01 12:20:57 "DELETE FROM table1 WHERE id=1;"
2018-01-01 12:21:32 "SELECT * FROM table2;"
2018-01-01 12:21:42 "SELECT * FROM table2;"
2018-01-01 12:21:57 "UPDATE table2 SET age=18 WHERE id=1;"
```

请用任意语言实现：获取每分钟执行次数最多的SQL语句
