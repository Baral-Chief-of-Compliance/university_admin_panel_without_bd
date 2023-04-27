<template>
    <div class="text-h3 py-6 mx-10 text-left">Добавить нагрузку для {{ name_t }} {{ patri_t }} {{ surname_t }}</div>

    <v-row class="d-flex justify-center my-5">
        <v-card v-show="add_workload" class="pa-6" color="green-accent-1">
            Нагрузка добавлена
        </v-card>
    </v-row>

    <div class="py-6 mx-10 d-flex justify-center">
        <v-col>
            <v-row class="ma-10" v-if="stage === 0">
                <v-radio-group v-model="name_dis">
                    <v-radio color="indigo"  v-for="d in disciplines"
                        :value="d.name_dis"
                        :label="`${d.name_dis}`"
                    >
                    </v-radio>                                 
                </v-radio-group>
            </v-row>

            <v-row class="ma-10" v-else-if="stage === 1">
                <v-radio-group v-model="name_control">
                    <v-radio color="indigo"  v-for="f in forms_of_work"
                        :value="f.name_control"
                        :label="`${f.name_control}`"
                    >
                    </v-radio>  
                </v-radio-group>
            </v-row>

            <v-row class="ma-10" v-else-if="stage === 2">
                <v-col>
                    <v-row>
                        <v-text-field v-model="course" type="number" label="Курс" color="indigo"></v-text-field>
                        <v-text-field v-model="hours" type="number" label="Часы" color="indigo"></v-text-field>
                        <v-text-field v-model="semester" type="number" label="Семестр" color="indigo"></v-text-field>
                        <v-text-field v-model="type_of_classes" type="text" label="Вид занятий" color="indigo"></v-text-field>
                    </v-row>
                    <v-row class="mt-10">
                        <v-btn block color="indigo" @click="create_workload()">
                            Добавить нагрузку
                        </v-btn>
                    </v-row>
                </v-col>


            </v-row>


            <v-row class="ma-10">
                <v-btn @click="exit_stage" color="gray" v-if="stage != 0 ">
                    Назад
                </v-btn>

                <v-spacer></v-spacer>
                <v-btn @click="enter_stage" color="indigo" v-if="stage !=2">
                    Вперед
                </v-btn>
            </v-row>
        </v-col>
    </div>
</template>

<script>
import axios from 'axios';
import disciplines_json from '@/data/disciplines.json'
import teachers_json from '@/data/teachers.json'


export default{
    data: () => ({
        name_t: "",
        patri_t: "",
        surname_t: "",
        add_workload: false,
        disciplines: disciplines_json,
        teachers: teachers_json,
        forms_of_work: [],
        workload: [],

        stage: 0,

        num_dis: "",
        num_work: "",
        num_t: "",
        course: "",
        hours: "",
        semester: "",
        type_of_classes: "",
        name_dis: "",
        name_control: ""
    }),

    methods: {
        get_teacher(){
            let teacher = this.teachers.find(item => item.num_t == this.$route.params.num_t)
            this.name_t = teacher.name_t,
            this.patri_t = teacher.patri_t,
            this.surname_t = teacher.surname_t,
            this.num_t = teacher.num_t,
            this.workload = teacher.workload
        },

        get_froms_of_work(name_dis){
            let discipline = this.disciplines.find(item => item.name_dis == name_dis)
            this.forms_of_work = discipline.forms_of_work
        },

        create_workload(){

            this.workload.push({
               "course":  this.course,
               "hours": this.hours,
               "name_control": this.name_control,
               "name_dis": this.name_dis,
               "semester": this.semester,
               "type_of_classes": this.type_of_classes
            })

            axios.post("http://127.0.0.1:5000/teachers", {
                teachers: this.teachers
            })

            this.add_workload = true,
            this.stage = 0,
            this.course = "",
            this.hours = "",
            this.semester = "",
            this.type_of_classes = "",
            this.num_dis = "",
            this.num_work = "",
            this.name_control = "",
            this.name_dis = ""
        },

        enter_stage(){
            if (this.stage === 0){
                this.get_froms_of_work(this.name_dis)
            }
            else if (this.stage === 0){
                this.add_workload = false
            }
            this.stage++
        },

        exit_stage(){
            this.stage--
        },
    },
    mounted(){
        this.get_teacher()
    }
}
</script>