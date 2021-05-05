var page_title = document.getElementsByTagName("title")[0].innerHTML.split(' - ')[0];
var sidebar_list = document.getElementById("sidebar_ul").getElementsByTagName("a");
var navbar_list = document.getElementById("navbar_ul").getElementsByTagName("a");
var my_home_button = document.getElementById('my_home_button');

console.log(page_title);
console.log(sidebar_list.length);


for (var i = 0; i < sidebar_list.length; i++) {
    console.log(sidebar_list[i].innerHTML );
    if (sidebar_list[i].innerHTML === page_title) {
        sidebar_list[i].classList.add("active");
        navbar_list[i].classList.add("active");
        navbar_list[i].classList.add("text-white");
        console.log(sidebar_list[i]);
        console.log(navbar_list[i]);
    } else {
        sidebar_list[i].parentElement.classList.add('non_visible');
    }
}

switch (page_title) {
    case 'Home':
        class_to_add = "btn-secondary";
        break;
    case 'Contact':
        class_to_add = "btn-success";
        break;
    case 'You Know Me?':
        class_to_add = "btn-danger";
        break;
    case 'Testimonials':
        class_to_add = "btn-warning";
        break;
    case 'Photos':
        class_to_add = "btn-info";
        break;
    case 'Projects':
        class_to_add = "btn-primary";
        break;
    case 'Monetary Metrics':
        class_to_add = "btn-dark";
}

my_home_button.classList.add(class_to_add);