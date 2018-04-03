var reg_list = ['A', 'B', 'C', 'D', 'E', 'F'];

// reg := 0
$('#btn-set0').click(function(){
    var reg = document.getElementById("reg").value.toUpperCase();
    if(!reg_list.includes(reg)){
        $('#msg_box').html("Registrador inexistente");
            var toastHTML = '<span> ERRO: Registrador Inexistente! </span>';
            M.toast({html: toastHTML});
    }else{
    $.post("/set-0-to-reg", { reg: reg }, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
    }
});

// reg := N
$('#btn-setN').click(function(){
    var reg = document.getElementById("reg").value.toUpperCase();
    var n = parseInt(document.getElementById("n_val").value.toUpperCase());
    $.post("/set-n-to-reg", { reg: reg, val: n }, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

// A := A + B
$('#btn-addBtoA').click(function(){
    $.post("/add-b-to-a", {}, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

// A := A + B usando C
$('#btn-addBtoAwC').click(function(){
    $.post("/add-b-to-a-with-c", {}, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

// A := B usando C
$('#btn-setBtoA').click(function(){
    $.post("/set-b-to-a", {}, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

// A := A x B usando C, D
$('#btn-multAwB').click(function(){
    $.post("/mult-a-with-b", {}, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

// Push to Stack
$('#btn-push').click(function(){
    $.post("/push", {val: 3}, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

// Pop from Stack
$('#btn-pop').click(function(){
    $.post("/pop", {}, function(data){
        var html = '';
        if(data.msg){
            $('#msg_box').html(data.msg);
            var toastHTML = '<span>'+ data.msg + '</span>\
                <button class="btn-flat toast-action">\
                    <i class="material-icons">close</i>\
                </button>';
            M.toast({html: toastHTML});
        }
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

$('#btn-testBgreaterA').click(function(){
    $.post( "/test-a-lower-than-b", {}, function(data){
        var html = '';
            $('#msg_box').html(data.result);
            var toastHTML = '<span>'+ data.result + '</span>\
                <button class="btn-flat toast-action">\
                    <i class="material-icons">close</i>\
                </button>';
            M.toast({html: toastHTML});
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

$('#btn-testBgreatereqA').click(function(){
    $.post( "/test-a-lower-eq-than-b", {}, function(data){
        var html = '';
            $('#msg_box').html(data.result);
            var toastHTML = '<span>'+ data.result + '</span>\
                <button class="btn-flat toast-action">\
                    <i class="material-icons">close</i>\
                </button>';
            M.toast({html: toastHTML});
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

$('#btn-fat').click(function(){
    var val = parseInt(document.getElementById("n_fat").value);
    $.post( "/factorial", { n: val }, function(data){
        var html = '';
        if(data.error){
            $('#msg_box').html(data.error);
            var toastHTML = '<span>'+ data.error + '</span>\
                <button class="btn-flat toast-action">\
                    <i class="material-icons">close</i>\
                </button>';
            M.toast({html: toastHTML});
        }
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

$('#btn-power').click(function(){
    $.post( "/power", { base: 5, exp: 2 }, function(data){
        var html = '';
        if(data.error){
            console.log('Error');
            $('#msg_box').html(data.error);
            var toastHTML = '<span>'+ data.error + '</span>';
            M.toast({html: toastHTML});
        }
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});

$('#btn-reset').click(function(){
    $.post( "/reset", {}, function(data){
        var html = '';
        $('#result').html('');
        for(let i = 0; i < data.response.length; i++){
            let entry = data.response[i];
            html += '<tr>';
            for (let key in entry.registers) {
                if (entry.registers.hasOwnProperty(key)) {
                    html += '<td> (' + entry.registers[key].signal + ', ' + entry.registers[key].magnitude + ') </td>';
                }
            }
            html += '<td>' + entry.stack + '</td>';
            html += '<td>' + entry.stack_pointer + '</td>';
            html += '</tr>';
        }
        $('#result').html(html);
    });
});