import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

record File(int size, String name) { }

public class Dir {
    public final String dirName;
    public final Dir parent;
    public final Map<String, Dir> subDir = new HashMap<>();
    public final List<File> files = new LinkedList<>();
    public int size = 0;

    public Dir(String dirName, Dir parent) {
        this.dirName = dirName;
        this.parent = parent;
    }

    public void addDir(String name, Dir d){
        subDir.put(name, d);
    }

    public void addFile(int fileSize, String fileName) {
        files.add(new File(fileSize, fileName));
    }

    public Dir subDir(String name) {
        return subDir.get(name);
    }

    public void calcSize() {
        files.forEach(file -> size += file.size());
        subDir.values().forEach(dir -> size += dir.size);
    }
}
