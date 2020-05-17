<template>
  <div>
    <p class='{{selectData}}'> Please select the file containing your followers' data </p>
    <input style="padding-left: 20px" class='{{file}}' id="file" ref="file" type="file" v-on:change="{{handleFile}}"/>
    <input type="file" ref="directory" webkitdirectory v-on:change="{{handleDirectory}}"/>
    <button style="padding-left: -20px" class='{{runPythonButton}}' @click="{{clearFile}}"> Clear File </button>

    <br>
    <button 
      @click="{{myMethod}}"
      style="margin-left: 10px; width: 394px;"
    >
      Analyze Follower Data 
    </button>
    <br v-if="{{rendering}}">
    <br v-if="this.rendering == true">
    <div class='parent' style="{width: 100%;}">
      <div class="loader" v-if="this.rendering == true"></div>
    </div>
    <p v-if="this.rendering == false && this.fileProcessed == true">File Processed: {{this.nameOfFile}}</p>
  </div>
</template>

<script>
export default {
  props: ['selectData', 'handleFile', 'handleDirectory', 'runPythonButton', 'clearFile', 'myMethod']
}
</script>

<style>

</style>