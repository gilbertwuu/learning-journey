        var learningNotes = __LEARNING_NOTES__;
        var learningBox = document.getElementById('learning-description');
        learningBox.replaceChildren();
        var note = learningNotes[id];
        if (note) {
          var level = document.createElement('p'); level.className='learning-level'; level.textContent=note[0]; learningBox.appendChild(level);
          ['目前已经理解的内容','还需要弄清楚的部分'].forEach(function(heading, i) {
            var h=document.createElement('h4');h.textContent=heading;learningBox.appendChild(h);
            var p=document.createElement('p');p.textContent=note[i+1];learningBox.appendChild(p);
          });
        }
