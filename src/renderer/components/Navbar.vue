<template>
  <div>
    <ul>
      <li @click="underline('followers', 'storyEngagement', 'stickerResponses')"
          id='followers'
      >
        Followers
      </li>

      <li @click="underline('stickerResponses', 'storyEngagement', 'followers')"
          id='stickerResponses'
      >
        Sticker Responses
      </li>

      <li @click="underline('storyEngagement', 'followers', 'stickerResponses')"
          id='storyEngagement'
      >
        Story Engagement
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  props: {
    msg: String
  },
  methods: {
    underline (primaryId, secondaryId, tertiaryId) {
      this.$store.state[secondaryId] = false;
      this.$store.state[tertiaryId] = false;
      this.$store.state[primaryId] = false;
      this.$store.state[primaryId] = this.$store.state[primaryId] === true ? false : true;
      document.getElementById(primaryId).style.textDecoration = this.$store.state[primaryId] === true ? "underline" : 'none';
      document.getElementById(secondaryId).style.textDecoration = this.$store.state[secondaryId] === true ? "underline" : 'none';
      document.getElementById(tertiaryId).style.textDecoration = this.$store.state[tertiaryId] === true ? "underline" : 'none';
    }
  }
};
</script>

<style scoped>
ul {
  list-style-type: none;
}

li {
  padding-bottom: 30px;
}

li #followers {
  text-decoration: underline;
}

li:hover {
  text-decoration: underline !important;
}

</style>