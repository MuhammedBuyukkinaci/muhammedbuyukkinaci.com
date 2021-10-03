// function Question(text,choices,answer){
//     this.text = text;
//     this.choices = choices;
//     this.answer = answer;
// }

// //Question prototyping

// Question.prototype.checkAnswer = function(answer){
//     return this.answer === answer;
// }

// //Quiz Consructor

// function Quiz(questions){
//     this.questions = questions;
//     this.score = 0;
//     this.questionIndex = 0;
// }

// //Quiz getQuestion
// Quiz.prototype.getQuestion = function(){
//     return this.questions[this.questionIndex];
// }

// //Quiz isFinish

// Quiz.prototype.isFinish = function() {
//     return this.questions.length === this.questionIndex;
// }

// //Quiz guess
// Quiz.prototype.guess = function(answer){
//     var question = this.getQuestion();

//     if(question.checkAnswer(answer) ){
//         this.score++;
//     }

//     this.questionIndex++;


// }

// var q01 = new Question("What is the current company that I work now?",["Turkcell",'Organon Analytics','UrbanStat','Analytica Solutions'],'UrbanStat');
// var q02 = new Question("Which programming language do I use most?",["C#",'JavaScript','Python','C++'],'Python');
// var q03 = new Question("Which programming language did I never use?",["C#",'Go','JavaScript','Python'],'Go');
// var q04 = new Question("What is my favorite Turkish football team?",["Galatasaray",'Fenerbahçe','Beşiktaş','İstanbul Başakşehir'],'Fenerbahçe');
// var q05 = new Question("Which Premier League Team do I support?",["Manchester City",'Manchester United','Chelsea','Arsenal'],'Manchester City');
// var q06 = new Question("Which menemen option is my favorite?",["Without onion and without pepper",'Without onion and with pepper','With onion and without pepper','With onion and with pepper'],'With onion and without pepper');
// var q07 = new Question("What OS do I often use? ",["Windows",'Ubuntu','Mac Sierra','Red Hat'],'Ubuntu');
// var q08 = new Question("How many minutes do I run in a week approximately? ",["200",'180','240','150'],'150');
// var q09 = new Question("Which ML framework do I prefer? ",["PyTorch",'MxNet','Onnx','TensorFlow'],'TensorFlow');
// var q10 = new Question("Which couple is used to build up this website? ",['Django - Python','ASP.NET Core - C#','Spring Boot - Java','Flask - Python'],'Django - Python');

// var questions = [q01,q02,q03,q04,q05,q06,q07,q08,q09,q10];

// //Start Quiz

// var quiz = new Quiz(questions);

// loadQuestion();

// function loadQuestion(){
//     if(quiz.isFinish()){
//         showScore();

//     }
//     else{

//         var question = quiz.getQuestion();
//         var choices = question.choices;
//         let speed = 40;
//         document.querySelector('#question').textContent = question.text;

//         //Inputing choices into buttons
//         for(var i=0; i< choices.length;i++){
//             var element = document.querySelector('#choice' + i);
//             element.innerHTML = choices[i];

//             guess('btn' +i, choices[i] );
//         }

//         showProgress();

//     }
// }

// function guess(id,guess){
//     var btn = document.getElementById(id);
//     btn.onclick = function(){
//         quiz.guess(guess);
//         loadQuestion();
//     }

// }

// function showScore(){
//     document.getElementById("buttons").remove();
//     document.querySelector('#progress').innerHTML = 'You have finished the quiz.';
//     var html_used = `<h2> Score </h2> <h4> ${quiz.score *10} </h4>`;
//     document.querySelector('.card-body').innerHTML = html_used;
// }

// function showProgress(){
//     var totalquestion = quiz.questions.length;
//     var questionNumber = quiz.questionIndex + 1;
//     document.querySelector('#progress').innerHTML = 'Question ' + questionNumber + ' of ' + totalquestion;
// }


