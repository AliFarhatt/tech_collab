import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalCloseButton,
    ModalBody,
    ModalFooter,
    Button,
    VStack,
    Input,
    Textarea,
    FormControl,
    FormLabel,
    Select,
    Spinner,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { updateProject } from "../../../services/UserApi";
import { toast } from "react-toastify";

const EditProjectModal = ({ isOpen, onClose, project, authUser, setAuthUser }) => {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [status, setStatus] = useState("");
    const [url, setUrl] = useState("");
    const [technologies, setTechnologies] = useState("");
    const [startDate, setStartDate] = useState("");
    const [endDate, setEndDate] = useState("");
    const [isSaving, setIsSaving] = useState(false);

    useEffect(() => {
        if (project) {
            setTitle(project.title || "");
            setDescription(project.description || "");
            setStatus(project.status || "");
            setUrl(project.url || "");
            setTechnologies((project.technologies || []).join(", "));
            setStartDate(project.start_date || "");
            setEndDate(project.end_date || "");
        }
    }, [project]);

    const handleUpdateProject = async () => {
        setIsSaving(true);
        const updatedProject = {
            title,
            description,
            status,
            url,
            technologies: technologies.split(",").map((tech) => tech.trim()),
            start_date: startDate,
            end_date: endDate,
        };

        try {
            const response = await updateProject(project.id, updatedProject);
            if (response.status === true) {
                const updatedProjects = authUser.user_projects.map((p) =>
                    p.id === project.id ? response.data : p
                );
                setAuthUser((prevUser) => ({
                    ...prevUser,
                    user_projects: updatedProjects,
                }));
                toast.success("Project updated successfully.");
                onClose();
            }
        } catch (error) {
            console.error("Error updating project:", error);
            toast.error(error.message);
        } finally {
            setIsSaving(false);
        }
    };

    const handleClose = () => {
        setTitle("");
        setDescription("");
        setStatus("");
        setUrl("");
        setTechnologies("");
        setStartDate("");
        setEndDate("");
        onClose();
    };

    return (
        <Modal isOpen={isOpen} onClose={handleClose}>
            <ModalOverlay />
            <ModalContent>
                <ModalHeader>Edit Project</ModalHeader>
                <ModalCloseButton />
                <ModalBody>
                    <VStack spacing={4}>
                        <FormControl isRequired>
                            <FormLabel>Title</FormLabel>
                            <Input
                                value={title}
                                onChange={(e) => setTitle(e.target.value)}
                            />
                        </FormControl>

                        <FormControl>
                            <FormLabel>Description</FormLabel>
                            <Textarea
                                value={description}
                                onChange={(e) => setDescription(e.target.value)}
                            />
                        </FormControl>

                        <FormControl>
                            <FormLabel>Status</FormLabel>
                            <Select
                                value={status}
                                onChange={(e) => setStatus(e.target.value)}
                            >
                                <option value="Ongoing">Ongoing</option>
                                <option value="Completed">Completed</option>
                                <option value="Paused">Paused</option>
                            </Select>
                        </FormControl>

                        <FormControl>
                            <FormLabel>Project URL</FormLabel>
                            <Input
                                value={url}
                                onChange={(e) => setUrl(e.target.value)}
                            />
                        </FormControl>

                        <FormControl>
                            <FormLabel>Technologies (comma-separated)</FormLabel>
                            <Input
                                value={technologies}
                                onChange={(e) => setTechnologies(e.target.value)}
                            />
                        </FormControl>

                        <FormControl>
                            <FormLabel>Start Date</FormLabel>
                            <Input
                                type="date"
                                value={startDate}
                                onChange={(e) => setStartDate(e.target.value)}
                            />
                        </FormControl>

                        <FormControl>
                            <FormLabel>End Date</FormLabel>
                            <Input
                                type="date"
                                value={endDate}
                                onChange={(e) => setEndDate(e.target.value)}
                            />
                        </FormControl>
                    </VStack>
                </ModalBody>

                <ModalFooter gap={2}>
                    <Button
                        colorScheme="blue"
                        onClick={handleUpdateProject}
                        isLoading={isSaving}
                        spinner={<Spinner size="sm" />}
                        loadingText="Saving"
                    >
                        Save
                    </Button>
                    <Button variant="ghost" onClick={handleClose}>
                        Cancel
                    </Button>
                </ModalFooter>
            </ModalContent>
        </Modal>
    );
};

export default EditProjectModal;
