<template>
  <div>
    <b-container>
      <b-form @submit="onSubmit" v-if="show">
        <b-form-group id="input-group-2" label="Team Name:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="team.name"
            required
            placeholder="Enter Team Name"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>
      <b-card class="mt-3" header="Current Teams">
        <b-list-group>
          <b-list-group-item
            v-for="(t, index) in teams"
            class="d-flex justify-content-between align-items-center"
            v-bind:key="index"
            >
            {{ t.name }}
            <b-badge variant="primary" pill>{{ t.score}} </b-badge>
          </b-list-group-item>
        </b-list-group>
      </b-card>
      <br>
      <ul>
          <li><router-link :to="{ name: 'RoundOne', params: {'teams': teams} }">Start</router-link></li>
      </ul>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'AddTeam',
  data () {
    return {
      team: {
        name: '',
        score: 0
      },
      show: true,
      teams: []
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      let newTeam = JSON.parse(JSON.stringify(this.team))
      this.teams.push(newTeam)
      alert(JSON.stringify(this.team))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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
