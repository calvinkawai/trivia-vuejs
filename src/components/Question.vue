<template>
<div class="Question">
  <b-container>
    <b-jumbotron>
      <template v-slot:lead>
        <h> Current Question </h>
        <br>
        {{ questionDes }}
      </template>
      <div>
        <b-img :src="this.img" fluid></b-img>
      </div>
      <b-list-group>
        <b-list-group-item :disabled="selected.includes(index)" :class="correct(index, answer)" v-for="(answer, index) in shuffledAnswers" v-bind:key="index" button=true v-on:click="chooseAnswer(index, answer)">
          {{ answer }}
        </b-list-group-item>
      </b-list-group>
      <b-list-group>
        <b-list-group-item button=true v-on:click="showAnswer()">
          Show Answer
        </b-list-group-item>
      </b-list-group>
    </b-jumbotron>
  </b-container>
</div>
</template>

<script>
export default {
  name: 'Question',
  data() {
    return {
      selected: [],
      shuffledAnswers: [],
      img: ''
    }
  },
  props: {
    questionDes: String,
    answers: Array,
    correctAnswer: String,
    increment: Function,
    selectedIndexs: Array,
    imageSrc: String
  },
  watch: {
    questionDes: function() {
      this.selected = []
      this.shuffle()
      this.img = this.imageSrc
    }
  },
  methods: {
    chooseAnswer: function(i, answer) {
      this.selected.push(i)
      if (answer === this.correctAnswer) {
        this.increment(1)
      } else {
        this.increment(0)
      }
    },
    correct: function(index, answer) {
      if (this.selected.includes(index) && answer === this.correctAnswer) {
        console.log('correct')
        return 'correct'
      }
      return 'random'
    },
    shuffle: function() {
      let i = this.answers.length - 1
      for (; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [this.answers[i], this.answers[j]] = [this.answers[j], this.answers[i]]
      }
      this.shuffledAnswers = this.answers
    },
    showAnswer: function() {
      let i = this.answers.length - 1
      for (; i >= 0; i--) {
        this.selected.push(i)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.correct {
  background-color: lightblue;
}
</style>
