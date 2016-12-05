
//Global Variables
var height = 256; // Size of Canvas
var width = 512; // Size of Canvas
var backgroundColor = 0x1099bb;
var num_lives = 3; // Number of lives
var previous = 1; // Previous note (if we dont want repetition).
                  // If we want repetition, change to 0
var intervalsize = 150; // Interval in which we want to create new notes


//Aliases
var Container = PIXI.Container,
    autoDetectRenderer = PIXI.autoDetectRenderer,
    loader = PIXI.loader,
    resources = PIXI.loader.resources,
    TextureCache = PIXI.utils.TextureCache,
    Texture = PIXI.Texture,
    Sprite = PIXI.Sprite;


//Create Pixi stage and renderer and add the
//renderer.view to the DOM
var stage = new Container();
renderer = autoDetectRenderer(width, height);
renderer.backgroundColor = backgroundColor;
document.body.appendChild(renderer.view);

// Object Containers we will use

var menu = new PIXI.DisplayObjectContainer();
var gameCore = new PIXI.DisplayObjectContainer();
var gameObjects = new PIXI.DisplayObjectContainer();
var lives = new PIXI.DisplayObjectContainer();

PIXI.loader
  .add([
      "game/images/quarter.png",
      "game/images/c_quarter.png",
      "game/images/clef.png",
      "game/images/heart.png"
  ])
  .on("progress", loadProgressHandler)
  .load(init);

function loadProgressHandler(loader, resource) {

    //Display the file `url` currently being loaded
    console.log("loading: " + resource.url);

    //Display the precentage of files currently loaded
    console.log("progress: " + loader.progress + "%");

    //If you gave your files names as the first argument
    //of the `add` method, you can access them like this
    //console.log("loading: " + resource.name);
}

function init()
{


    console.log("All files loaded");

    var style_title = {
        fontFamily : 'Courier',
        fontSize : '60px',
        fontStyle : 'italic',
        fontWeight : 'bold',
        fill : '#F7EDCA',
        stroke : '#4a1850',
        strokeThickness : 5,
        dropShadow : true,
        dropShadowColor : '#000000',
        dropShadowAngle : Math.PI / 6,
        dropShadowDistance : 6,
        wordWrap : true,
        wordWrapWidth : 440
    };
    var style_subtitle = {
        fontFamily : 'Courier',
        fontSize : '30px',
        fontStyle : 'italic',
        fontWeight : 'bold',
        fill : '#F7EDCA',
        stroke : '#4a1850',
        strokeThickness : 5,
        dropShadow : true,
        dropShadowColor : '#000000',
        dropShadowAngle : Math.PI / 6,
        dropShadowDistance : 6,
        wordWrap : true,
        wordWrapWidth : 440
    };

    var title = new PIXI.Text('Key Learning',style_title);
    title.x = 30;
    title.y = 20
    var subtitle_play = new PIXI.Text('play', style_subtitle); //PIXI.Sprite.fromImage('images/play_button.png');
    subtitle_play.x = 120;
    subtitle_play.y = 100;

    subtitle_play.interactive = true;
    subtitle_play.on('mousedown', setup);
    subtitle_play.on('touchstart', setup);
    var subtitle_highScores = new PIXI.Text('high scores', style_subtitle)
    subtitle_highScores.x = 120;
    subtitle_highScores.y = 140;
    var subtitle_badges = new PIXI.Text('badges', style_subtitle);
    subtitle_badges.x = 120;
    subtitle_badges.y = 180;

    menu.addChild(title);
    menu.addChild(subtitle_play);
    menu.addChild(subtitle_highScores);
    menu.addChild(subtitle_badges);

    stage.addChild(menu);

    renderer.render(stage);

}



function setup() {

    // When we change "screens" we have to set objects visible so we can seem them
    menu.visible = false;
    gameObjects.visible = true;
    lives.visble = true;
    gameCore.visible = true;

    // Everytime we start the game, lives_left returns to what is should be
    lives_left = num_lives;

    // We create a clef and add it to the game core objects
    clef = new Sprite(resources["{% static 'game/images/clef.png' %}"].texture);
    clef.height = 1/2 * height;
    clef.width = width;
    clef.position.set(0, height/2 - (clef.height)/2);
    gameCore.addChild(clef);

    // We create the score text and we add it to the game core objects
    scoreText = new PIXI.Text('Score: 0');
    scoreText.position.set(0, 0)
    gameCore.addChild(scoreText);

    stage.addChild(gameCore);

    for (var i = 0; i < num_lives; i++)
    {
        var heart = new Sprite(resources["{% static 'game/images/heart.png' %}"].texture);
        heart.height = 1/15 * height;
        heart.width = heart.height;
        var offset = width / 50 + heart.width;
        heart.position.set(width - (offset +  (i * heart.width)), height/100 );
        //console.log("Heart " + i + " x: "+ heart.x + " y: "+ heart.y); // DEBUG
        lives.addChild(heart);
    }
    stage.addChild(lives);

    // DEBUG
    //console.log("Clef X: "+ clef.x + " Clef Y: "+clef.y + "Size: " + clef.height);

    //Render the stage
    renderer.render(stage);

    //We will need this to count frames
    frameCounter = 0;
    //Start gameObjects Loop
    gameObjectsLoop();
    init();
}

function gameObjectsLoop()
{
    // We lost...

    if (lives_left <= 0)
    {
        return;
    }
    // DEBUG
    //console.log("Frame Counter: " + frameCounter);

    // Update frameCounter
    frameCounter += 1;

    var lines = clef.height / 16;
    var notes_w = 1/20 * width;
    var notes_h = 1/10 * height;

    // Starting from bottom to up, this is how different notes are placed
    // (in relation to the sheet):

     C = clef.y + lines * 15 - notes_h - height/100;
     D = clef.y + lines * 14 - notes_h - height/100;
     E = clef.y + lines * 13 - notes_h - height/100;
     F = clef.y + lines * 12 - notes_h - height/100;
     G = clef.y + lines * 11 - notes_h - height/100;
     A = clef.y + lines * 10 - notes_h - height/100;
     B = clef.y + lines * 09 - notes_h - height/100;

    // Spawn more notes every "intervalsize"
    if (frameCounter == 1 || everyinterval(intervalsize))
    {
        var maximum = 15; // This is a C
        var minimum = 9;  // This is an A

        // Randomly choose next note line
        var next_note_line = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
        // If previous != 0 we dont allow repetitions
        while (next_note_line == previous && previous)
        {
            next_note_line = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
        }
        if (previous)
            previous = next_note_line;

        // Sets next_note_y to the y value where that we want next note  to have
        next_note_y = clef.y + lines * next_note_line - notes_h - height/100;

        // Then it is a C, so we have to assign a different image
        if (next_note_line == maximum)
        {
            var c_quarter = new Sprite(resources["{% static 'game/images/c_quarter.png' %}"].texture);
            c_quarter.height = notes_h;
            c_quarter.width = notes_w;
            c_quarter.position.set(width, next_note_y);
            gameObjects.addChild(c_quarter);
        }
        // Is a regular quarter note
        else
        {
            var quarter = new Sprite(resources["{% static 'game/images/quarter.png' %}"].texture);
            quarter.height = notes_h;
            quarter.width = notes_w;
            quarter.position.set(width, next_note_y);
            gameObjects.addChild(quarter);
        }


    }
    // DEBUG
    //for (var i = 0; i< gameObjects.children.length; i++)
    //    console.log(gameObjects.children[i]);
    // For every note in the gameObjects
    for (var i = 0; i < gameObjects.children.length; i++)
    {
        // We make them move
        gameObjects.children[i].x -= 1;
        // If we x <= 0, then it moves out of screen and we lose a life. So:
        if (gameObjects.children[i].x <= 0)
        {
            // We remove the note from the gameObjects objects
            gameObjects.children.splice(i,1);
            // We decrement the lives left
            lives_left -= 1;
            // We remove 1 heart from the gameObjects objects so it desappears from screen
            lives.children.splice(lives_left, 1);


        }
    }
    // We update the score
    scoreText.setText('Score: '+frameCounter);
    stage.addChild(gameCore);
    stage.addChild(gameObjects);
    //Render the stage
    renderer.render(stage);
    // Loop this function @ 60 fps
    requestAnimationFrame(gameObjectsLoop);


}

window.addEventListener("keydown", checkKeyDown, true);

function checkKeyDown(ev)
{
    // Map Keys to lines:
    var code = ev.keyCode;
    console.log(code);
    // If there are any notes on scree... if not, we can assume it was a misclick and don't punish the player
    if (gameObjects.children.length > 1)
    {
        console.log("I am pressing: " + code)
        switch (code)
        {
            case 65: test(C); break; // A pressed on KEYBOARD
            case 83: test(D); break; // S pressed on KEYBOARD
            case 68: test(E); break; // D pressed on KEYBOARD
            case 70: test(F); break; // F pressed on KEYBOARD
            case 71: test(G); break; // G pressed on KEYBOARD
            case 72: test(A); break; // H pressed on KEYBOARD
            case 74: test(B); break; // J pressed on KEYBOARD
            default: break;
        }
    }


}

function test(note)
{
    console.log("I am pressing: " + note + " and checking against: "+ gameObjects.children[0].y);
    if (gameObjects.children[0].y == note)
        gameObjects.children.splice(0, 1);

    else {
        lives_left -=1;
        lives.children.splice(lives_left,1);

    }
    renderer.render(stage);
}

function everyinterval(n) {
    if ((frameCounter / n) % 1 == 0)
    {
        intervalsize = 150;
        return true;
    }
    return false;

}
