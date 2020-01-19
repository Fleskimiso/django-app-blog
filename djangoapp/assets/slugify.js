const title = document.querySelector('input[name=title]');
const slug = document.querySelector('input[name=slug]');

console.log(" script running lol why this is not working");
console.log(slug);


const slugify = (val) =>{
    return val.toString().toLowerCase().trim().replace(/&/g, '-and-' )  //replace & with g and
    .replace(/[\s\W-]+/g, '-') //replaces spaces and non word chars and dashed with a single dash
};

title.addEventListener('keyup',(e) =>{
    slug.setAttribute('value', slugify(title.value));
});

