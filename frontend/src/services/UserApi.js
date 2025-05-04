import * as HttpRequest from './HttpRequest';
import * as e from "../Endpoints";

export const getUserBase64Cv = async (signal) => {
    return await HttpRequest.get(e.CRUD_USER + "/cv-base64", null, 'token', signal);
};

export const searchUsers = async (query, signal) => {
    return await HttpRequest.get(e.CRUD_USERS + `/search?search=${query}`, null, 'token', signal);
};

export const followUser = async (body, signal) => {
    return await HttpRequest.post(e.CRUD_USER + `/follow`, body, 'token', signal);
};

export const unfollowUser = async (body, signal) => {
    return await HttpRequest.post(e.CRUD_USER + `/unfollow`, body, 'token', signal);
};

export const getUser = async (userId, signal) => {
    return await HttpRequest.get(e.CRUD_USER + `/${userId}`, null, 'token', signal);
};

export const editSkills = async (body, signal) => {
    return await HttpRequest.patchApi(e.CRUD_USER + "/skills", body, 'token', signal);
};

export const addProject = async (body, signal) => {
    return await HttpRequest.post(e.CRUD_USER + `/project`, body, 'token', signal);
};
export const updateProject = async (projectId, body, signal) => {
    return await HttpRequest.patchApi(
        e.CRUD_USER + `/project/${projectId}`,
        body,
        'token',
        signal
    );
};

export const getUsersByVectorID = async (body, signal) => {
    return await HttpRequest.post(e.CRUD_USERS + `/get-by-vector-ids`, body, 'token', signal);
};