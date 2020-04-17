<template>
  <div class='parent' v-if="this.$store.state.followers === true">
    <p class='selectData'> Please select the file containing your followers' data </p>
    <input style="padding-left: 20px" class='file' id="file" ref="file" type="file" v-on:change="handleFile('followers')"/>
    <input type="file" ref="directory" webkitdirectory v-on:change="handleDirectory()"/>
    <button style="padding-left: -20px" class='runPythonButton' @click="clearFile('followers')"> Clear File </button>

    <br>
    <button 
      @click="myMethod"
      style="margin-left: 10px; width: 394px;"
    >
      Analyze Follower Data 
    </button>
    <br v-if="this.rendering == true">
    <br v-if="this.rendering == true">
    <div class='parent' style="{width: 100%;}">
      <div class="loader" v-if="this.rendering == true"></div>
    </div>
    <p v-if="this.rendering == false && this.fileProcessed == true">File Processed: {{this.nameOfFile}}</p>
  </div>


  <div class='parent' v-else-if="this.$store.state.stickerResponses === true">
    <p class='selectData'> Please select the screenshots containing your sticker response data </p>
    <input class='file' id="file" ref="file" type="file" v-on:change="handleFile('stickers')" multiple />
    <input type="file" ref="directory" webkitdirectory v-on:change="handleDirectory()"/>
    <button class='runPythonButton' @click="clearFile('stickers')"> Clear File </button>
    <br>
    <button 
      @click="sticker"
      style="margin-left:-8px; width: 398px;"
    >
      Analyze Sticker Responses
    </button>
    <br v-if="this.rendering == true">
    <br v-if="this.rendering == true">
    <div class='parent' style="{width: 100%;}">
      <div class="loader" v-if="this.rendering == true"></div>
    </div>
    <p v-if="this.rendering == false && this.picsProcessed == true">Pictures Processed: {{this.numberOfPictures}}</p>
  </div>

  <div class='parent' v-else-if="this.$store.state.storyEngagement === true">
    <p class='selectData'> Please select the file containing your story engagement data </p>
    <input class='file' type="file"/>
    <button class='runPythonButton'> Analyze Story Engagement </button>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

export default {
  name: "Main",
  props: {
    msg: String
  },
  data () {
    return {
      rendering: false,
      fileProcessed: false,
      picsProcessed: false,
      nameOfFile: '',
      numberOfPictures: 0,
      directory: '$HOME'
    }
  },
  methods: {
    handleDirectory() {
      this.directory = this.$refs.directory.files[0].path
    },
    clearFile (file) {
      document.getElementById("file").value = ''

      if (file === 'followers') {
        this.fileProcessed = false
      }

      else if (file === 'stickers') {
        this.picsProcessed = false
      }
    },
    async handleFile(type){
      if (type === 'followers') {
        this.file = this.$refs.file.files[0];
      }
      else if (type === 'stickers') {
        this.file = this.$refs.file.files;
      }
    },
    async myMethod () {
      this.rendering = true
      
      let form_data =  new FormData();
      form_data.append('file', this.file)
            
      await axios.post(
        `http://localhost:5000/submit/?path=${this.directory}`,
        form_data,
        {
          headers: {
            'Content-type': 'multipart/form-data'
          }
        } 
      )
      .then((data) => {
        this.nameOfFile = this.file.name
        this.clearFile ()
        })
      .catch((e) => console.log(e))

      this.rendering = false
      this.fileProcessed = true
    },
    async sticker () {
      let form_data =  new FormData();
      this.rendering = true

      for (let i = 0; i < this.file.length; i++) {
        form_data.append('file', this.file[i])
        }

      this.numberOfPictures = this.file.length

      await axios.post(
        `http://localhost:5000/stickers/?path=${this.directory}`,
        form_data,
        {
          headers: {
            'Content-type': 'multipart/form-data'
          }
        }
      )
      .then((data) => {
        this.clearFile ()
        console.log(data)
      })
      .catch((e) => console.log(e))

      this.rendering = false
      this.picsProcessed = true
    }
  },
};
</script>

<style scoped>
.parent {
  display: inline-block;
  justify-content: center;
}
.file {
  width: 200px;
  height: 30px;
  justify-self: center;
}
.selectData {
  height: 20px;
}
.runPythonButton {
  width: 190px;
  height: 20px;
}
.loader {
  border: 10px solid #f3f3f3; /* Light grey */
  border-top: 10px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>