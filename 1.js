$(document).ready(
    function get_data() {
        $.ajax(
            {
                url: "data.json",
                type: "GET",
                dataType: "json",
                async: true,
                success: function(data){
                    html = "";
                    for (var i=0; i<data.length; i++){
                        html = html + "<tr><td>" + data[i].name +
                        "</td> <td>" + data[i].age +
                        "</td> <td><input type='button' value='delete'/></td></tr>"
                    }

                    $("tbody").append(html);

                    $("input").on("click", function(event){
                        $(event.target).parent().parent().remove();
                    })
                },
                error: function () {
                    alert("请求失败");
                }

            }
        )
    }
);