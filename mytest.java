/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package KTPM2013;

/**
 *
 * @author autorunx
 */
import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;
import junit.framework.TestCase;

public class mytest extends TestCase {

    public mytest(String name) {
        super(name);
    }

    /**
     * Xac nhan rang name duoc the hien dung dinh dang
     */
    public void testGetFullName() {
        Person p = new Person("Aidan", "Burke");
        assertEquals("Aidan Burke", p.getFullName());
    }

    /**
     * Xac nhan rang nulls da duoc xu ly chinh xac
     */
    public void testNullsInName() {
        Person p = new Person(null, "Burke");
        assertEquals("? Burke", p.getFullName());

        p = new Person("Tanner", null);
        assertEquals("Tanner ?", p.getFullName());
    }
}
