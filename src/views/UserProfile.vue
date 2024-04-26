<template>
    <div>
        <h1>{{ user.username }}'s Profile</h1>
        <div>
            <p>{{ user.firstname }} {{ user.lastname }}</p>
            <p>Location: {{ user.location }}</p>
            <p>Biography: {{ user.biography }}</p>
            <button @click="followUser">{{ isFollowing ? 'Following' : 'Follow' }}</button>
            <p>Followers: {{ user.follower_count }}</p>
        </div>
        <div v-if="posts.length">
            <h2>Posts</h2>
            <div v-for="post in posts" :key="post.id">
                <p>{{ post.caption }}</p>
                <img :src="post.photo" alt="post photo" />
            </div>
        </div>
        <div v-else>
            <p>No posts available.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            user: {},
            posts: [],
            isFollowing: false,
        };
    },
    computed: {
        userId() {
            return this.$route.params.user_id;
        },
    },
    mounted() {
        this.fetchUserProfile();
        this.fetchUserPosts();
        this.checkFollowingStatus();
    },
    methods: {
        async fetchUserProfile() {
            try {
                const response = await axios.get(`/api/v1/users/${this.userId}`, {
                    headers: {
                        Authorization: `Bearer ${this.getAuthToken()}`,
                    },
                });
                this.user = response.data;
            } catch (error) {
                console.error('Failed to fetch user profile:', error);
            }
        },
        async fetchUserPosts() {
            try {
                const response = await axios.get(`/api/v1/users/${this.userId}/posts`, {
                    headers: {
                        Authorization: `Bearer ${this.getAuthToken()}`,
                    },
                });
                this.posts = response.data;
            } catch (error) {
                console.error('Failed to fetch user posts:', error);
            }
        },
        async followUser() {
            try {
                const response = await axios.post(`/api/users/${this.userId}/follow`, {}, {
                    headers: {
                        Authorization: `Bearer ${this.getAuthToken()}`,
                    },
                });
                if (response.status === 200) {
                    this.isFollowing = true;
                    this.user.follower_count += 1;
                }
            } catch (error) {
                console.error('Failed to follow user:', error);
            }
        },
        checkFollowingStatus() {
            // Implement logic to check if the logged-in user is already following this user
            // and set the `isFollowing` data property accordingly.
        },
        getAuthToken() {
            // Implement method to retrieve JWT token
            return localStorage.getItem('authToken');
        },
    },
};
</script>
