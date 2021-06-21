<template>
<div>
  <b-container>
    <b-card class="mt-3" header="Teams">
      <b-list-group>
        <b-list-group-item v-for="(t, index) in teams" class="d-flex justify-content-between align-items-center" v-bind:key="index">
          {{ t.name }}
          <b-badge variant="primary" pill>{{ t.score }} </b-badge>
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </b-container>
  <b-container>
    <b-card-group>
      <b-card class="card align-items-center mt-3" v-for="(c, index) in categoryQuestionSet" v-bind:key="index">
        {{ c.name }}
        <div class="mt-3">
          <b-button-group>
            <b-button v-for="(question, i) in categoryQuestionSet[index].easy" v-bind:key="i" variant="success" v-on:click="chooseQuestion(question, 3)" :pressed.sync="question.state" :disabled="question.state">
              3
            </b-button>
          </b-button-group>
        </div>
        <div class="mt-3">
          <b-button-group>
            <b-button v-for="(question, i) in categoryQuestionSet[index].medium" v-bind:key="i" variant="info" v-on:click="chooseQuestion(question, 5)" :pressed.sync="question.state" :disabled="question.state">
              5
            </b-button>
          </b-button-group>
        </div>
        <div class="mt-3">
          <b-button-group>
            <b-button v-for="(question, i) in categoryQuestionSet[index].hard" v-bind:key="i" variant="warning" v-on:click="chooseQuestion(question, 8)" :pressed.sync="question.state" :disabled="question.state">
              8
            </b-button>
          </b-button-group>
        </div>
      </b-card>
    </b-card-group>
  </b-container>

  <b-container>
    <b-card class="mt-3">
      <b-list-group>
        <b-list-group-item class="d-flex justify-content-between align-items-center">
          First team to answer: {{ this.teams[this.currentTeam].name }}
        </b-list-group-item>
        <b-list-group-item class="d-flex justify-content-between align-items-center">
          Next team to answer: {{ this.teams[this.nextTeam].name }}
        </b-list-group-item>
      </b-list-group>
      <br>
      <Question :questionDes="currentQuestion.questionDes" :answers="currentQuestion.answers" :correctAnswer="currentQuestion.correctAnswer" :increment="increment" :selectedIndexs="currentQuestion.selectedIndexs"
        :imageSrc="currentQuestion.imageSrc" />
    </b-card>
  </b-container>
</div>
</template>

<script>
import Question from './Question.vue'
import round1 from '../assets/Round1.json'
export default {
  name: 'RoundOne',
  components: {
    Question
  },
  data() {
    return {
      teams: this.$route.params.teams,
      currentTeam: 0,
      nextTeam: 1,
      categoryQuestionSet: round1,
      answeredCurrentQuestion: 0,
      currentQuestion: {
        questionDes: '',
        answers: [],
        correctAnswer: '',
        point: 0,
        currentQuestion: [],
        imageSrc: ''
      }
    }
  },
  methods: {
    chooseQuestion: function(question, point) {
      if (question != null & question.state) {
        this.currentQuestion.questionDes = question.question
        this.currentQuestion.answers = [...question.incorrectAnswers, question.correctAnswer]
        this.currentQuestion.correctAnswer = question.correctAnswer
        if (question.img === '') {
          this.currentQuestion.imageSrc = ''
        } else {
          this.currentQuestion.imageSrc = require('@/assets/' + question.img)
        }
        this.currentQuestion.points = point
        this.currentQuestion.selectedIndexs = []
      }
      question.state = true
      this.answeredCurrentQuestion = 0
      this.currentTeam = this.next(this.currentTeam)
      this.nextTeam = this.next(this.nextTeam)
    },
    increment(isCorrect) {
      if (isCorrect === 1 & this.answeredCurrentQuestion === 0) {
        this.teams[this.currentTeam].score += this.currentQuestion.points
      } else if (isCorrect === 1 & this.answeredCurrentQuestion === 1) {
        this.teams[this.nextTeam].score += (this.currentQuestion.points -
          this.currentQuestion.points / 2)
      } else if (isCorrect === 0 & this.answeredCurrentQuestion === 1) {
        this.teams[this.nextTeam].score -= 1
      }
      this.answeredCurrentQuestion++
    },
    next(current) {
      if (current === this.teams.length - 1) {
        current = 0
      } else {
        current += 1
      }
      return current
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
</style>
